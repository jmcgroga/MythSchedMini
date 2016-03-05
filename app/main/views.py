from __future__ import print_function

from flask import Flask, render_template, jsonify, request, send_file, redirect, url_for
from flask.ext.script import Manager
from flask.ext.bootstrap import Bootstrap

from flask import current_app as app

from blist import blist

from datetime import datetime
from collections import defaultdict

from MythTV import *

from . import main

import pytz
eastern = pytz.timezone('US/Eastern')

import os
import socket
import pipes
from urlparse import urljoin, urlparse
from base64 import b64encode, b64decode

be = MythBE()
db = MythDB()

deleted = set()

def query(sql, params = None):
    with db as cursor:
        if params:
            cursor.execute(sql, params)
        else:
            cursor.execute(sql)

    for r in cursor:
        yield r

def getProgramStorageFileName(program):
    fullpath = ''
    if program and program.programid:
        with db as cursor:
            cursor.execute("""select distinct r.programid, sg.dirname, r.basename from recorded as r left join storagegroup as sg on r.storagegroup=sg.groupname where r.programid=%s""", (program.programid,))
        for r in cursor:
            thispath = os.path.join(r[1], r[2])
            if os.path.exists(thispath):
                fullpath = thispath
                break
    return fullpath

def getWatchNowDirectoryForProgramId(programid):
    return os.path.join(app.config['WATCH_NOW_DEST_DIR'], programid)

def watchProgram(program, title, subtitle):
    fullpath = getProgramStorageFileName(program)
    output_directory = getWatchNowDirectoryForProgramId(program.programid)
    url = ''
    if fullpath:
        url = urljoin(app.config['WATCH_NOW_BASE_URL'], program.programid)
        prog_url = urlparse(url).path
        params = {
            'ffmpeg_command' : pipes.quote(app.config['FFMPEG_COMMAND']),
            'input_file' : pipes.quote(fullpath),
            'segmenter_command' : pipes.quote(app.config['SEGMENTER_COMMAND']),
            'url' : pipes.quote(prog_url),
            'output_directory' : pipes.quote(output_directory)
        }
        index_file = os.path.join(output_directory, 'index.html')

        if not os.path.exists(index_file):
            cmd = app.config['WATCH_NOW_CONVERTER'] % (params)
            try:
                if not os.path.exists(output_directory):
                    os.makedirs(output_directory)
                with open(index_file, 'w') as outfile:
                    print(render_template('watchnow_program.html',
                                          title = title,
                                          subtitle = subtitle,
                                          width = 1280,
                                          height = 720,
                                          url = url), file=outfile)
                app.config['COMMAND_QUEUE'].put(('convert', (cmd, output_directory)))
            except:
                print('Unable to create directory:', output_directory)
    return url

def sortprograms(p, reverse=True):
    return sorted(p, key=lambda x: x.starttime, reverse=reverse)

def sortMissingEpisodeNumber(programs):
    missing = [ p for p in programs if not p.episode ]

    if missing:
        trimmed = [ p for p in programs if p.episode ]
        for m in missing:
            inindex = -1
            for i,p in enumerate(trimmed):
                if p.starttime > m.starttime:
                    inindex = i
                    break
            if inindex < 0:
                trimmed.append(m)
            else:
                trimmed.insert(inindex, m)
        return trimmed

    return programs

def groupprograms(programs):
    shows = defaultdict(lambda: blist())
    deleted = globals().get('deleted')
    still_deleted = set(deleted)

    for p in programs:
        if p.programid in still_deleted:
            still_deleted.discard(p.programid)
        else:
            shows[p.title].append(p)

    globals()['deleted'] = deleted - still_deleted

    for k,v in shows.items():
        episodes = sortMissingEpisodeNumber(sorted(v, key=lambda x: x.episode))
        season = ''
        newEpisodes = []
        for p in episodes:
            if p.season == 0 or season == p.season:
                newEpisodes.append(('', p))
            else:
                season = p.season
                newEpisodes.append((season, p))
        shows[k] = newEpisodes

    return shows

@main.route('/')
def upcoming():
    recording = [ be.getCurrentRecording(str(recorder)) for recorder in be.getRecorderList() if be.isRecording(recorder) ]
    upcoming = sortprograms(be.getUpcomingRecordings(), reverse=False)

    skipping = sortprograms([ p for p in be.getPendingRecordings() if p.recstatus != -1 and p.recstatus != -2 ], reverse=False)

    conflicts = sortprograms([ p for p in be.getPendingRecordings() if p.recstatus == 7 ], reverse=False)

    return render_template('upcoming.html',
                           recording = recording,
                           upcoming = upcoming,
                           skipping = skipping,
                           conflicts = conflicts,
                           tz = eastern,
                           now = datetime.now(tz=eastern),
                           today = datetime.now().date())

@main.route('/deleteProgram')
def deleteProgram():
    chanid = request.args.get('chanid', '')
    starttime = request.args.get('starttime', '')

    if chanid and starttime:
        program = be.getRecording(chanid, starttime)
        if program:
            output_directory = getWatchNowDirectoryForProgramId(program.programid)

            dest_directory = app.config.get('WATCH_NOW_DELETE_DIR')

            if output_directory and dest_directory:
                dest_directory = os.path.join(dest_directory, program.programid)
                app.config['COMMAND_QUEUE'].put(('move', (output_directory, dest_directory)))
            
            deleted.add(program.programid)
            program.delete(force=True)

    return redirect(url_for('main.recorded'))

@main.route('/recorded')
def recorded():
    with db as cursor:
        cursor.execute('select r.programid from recorded as r where transcoded=1')

    return render_template('recorded.html', 
                           programs = groupprograms(be.getRecordings()),
                           transcoded = { i[0] for i in cursor },
                           tz = eastern)

@main.route('/schedule')
def schedule():
    return render_template('schedule.html',
                           programs = sortprograms(be.getScheduledRecordings(), reverse=False),
                           tz = eastern)

@main.route('/add_schedule')
def add_schedule():
    return render_template('add_schedule.html')

@main.route('/status')
def status():
    ip = app.config['IP']
    return render_template('status.html',
                           ip = ip)

@main.route('/backend_status')
def backend_status():
    status = 'Error'
    try:
        uptime = be.getUptime().seconds
        if uptime > 0:
            status = '';
    except:
        pass
    return jsonify(status = status)

@main.route('/search_title')
def search_title():
    title = request.args.get('title')
    if title:
        with db as cursor:
            cursor.execute("""select distinct p.title, c.channum, c.name from program as p join channel as c on p.chanid=c.chanid where p.title like %s order by p.title""", ('%%%s%%' % (title),))
        starts = []
        rest = []
        for r in cursor:
            if r[0].startswith(title):
                starts.append(r)
            else:
                rest.append(r)
        return jsonify(result = starts + rest)
    return jsonify(result = [])

@main.route('/artwork/<title>')
def artwork(title):
    filename = os.path.join(app.config['ARTWORK_DIR'], '%s.png' % (title))
    return send_file(filename, mimetype='image/png')

@main.route('/watchnow/wait/<programid>/<title>/<subtitle>/<url>')
def watchnow_wait(programid, title, subtitle, url):
    url = b64decode(url)
    directory = getWatchNowDirectoryForProgramId(programid)

    if os.path.exists(os.path.join(directory, 'prog_index.m3u8')) and os.path.exists(os.path.join(directory, 'fileSequence2.ts')):
        return redirect(url)

    return render_template('watchnow_wait.html',
                           programid = directory,
                           title = title,
                           subtitle = subtitle,
                           url = url)

@main.route('/watchnow/watch/<chanid>/<recstartts>')
def watchnow_watch(chanid, recstartts):
    program = be.getRecording(chanid, recstartts)
    url = watchProgram(program, program.title, program.subtitle)
    if url:
        return redirect(url_for('main.watchnow_wait',
                                programid = program.programid,
                                title = program.title,
                                subtitle = program.subtitle,
                                url = b64encode(url)))
    return redirect(url_for('main.recorded'))

@main.route('/live')
def live():
    programs = query("""select c.channum, c.callsign, p.title, p.subtitle, p.starttime, p.endtime, p.programid from program as p left join channel as c on p.chanid = c.chanid  where starttime < now() and endtime > now() order by cast(c.channum as unsigned)""")
    return render_template('live.html',
                           programs = programs)

@main.route('/watchnow/live/<channum>/<title>/<subtitle>')
def watchnow_live(channum, title, subtitle):
    url = urljoin(app.config['WATCH_NOW_BASE_URL'], 'live')
    if url:
        return redirect(url_for('main.watchnow_wait',
                                programid = 'live',
                                title = title,
                                subtitle = subtitle,
                                url = b64encode(url)))
    return redirect(url_for('main.live'))

@main.route('/poke')
def poke():
    return jsonify()
