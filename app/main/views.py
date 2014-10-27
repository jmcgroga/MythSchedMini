from __future__ import print_function

from flask import Flask, render_template, jsonify, request
from flask.ext.script import Manager
from flask.ext.bootstrap import Bootstrap

from datetime import datetime

from MythTV import *

from . import main

import pytz
eastern = pytz.timezone('US/Eastern')

import socket
ip = socket.gethostbyname(socket.gethostname())

be = MythBE()
db = MythDB()

def sortprograms(p, reverse=True):
    return sorted(p, key=lambda x: x.starttime, reverse=reverse)

@main.route('/')
def upcoming():
    recording = [ be.getCurrentRecording(str(recorder)) for recorder in be.getRecorderList() if be.isRecording(recorder) ]
    upcoming = sortprograms(be.getUpcomingRecordings(), reverse=False)

    skipping = sortprograms([ p for p in be.getPendingRecordings() if p.recstatus != -1 ], reverse=False)

    return render_template('upcoming.html',
                           recording = recording,
                           upcoming = upcoming,
                           skipping = skipping,
                           tz = eastern, 
                           today = datetime.now().date())

@main.route('/deleteProgram')
def deleteProgram():
    chanid = request.args.get('chanid', '')
    starttime = request.args.get('starttime', '')

    if chanid and starttime:
        program = be.getRecording(chanid, starttime)
    
        if program:
            program.delete(force=True)

    #TODO: Wait for program to be deleted

    return render_template('recorded.html', 
                           programs = sortprograms(be.getRecordings()),
                           tz = eastern)

@main.route('/recorded')
def recorded():
    return render_template('recorded.html', 
                           programs = sortprograms(be.getRecordings()),
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

@main.route('/poke')
def poke():
    return jsonify()
