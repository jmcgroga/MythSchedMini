from __future__ import print_function

import os
import sys

from subprocess import Popen, PIPE
from mythschedmini.mixins import power_mixin

class PowerProcess(object):
    def start(self):
        self.p = Popen([ sys.executable, __file__ ], stdin = PIPE, env = { 'PYTHONPATH' : os.path.abspath(os.path.join(os.path.dirname(__file__), '..')) })

    def preventSleep(self, msg = None):
        if msg:
            self.p.stdin.write('sleep:%s\n' % (msg))
        else:
            self.p.stdin.write('sleep\n')

    def restoreSleep(self):
        self.p.stdin.write('wake\n')

    def processCommands(self):
        line = sys.stdin.readline().strip()

        while line:
            if line.startswith('sleep'):
                split_line = line.split(':', 2)
                if len(split_line) == 2:
                    self._preventSleep(split_line[1])
                else:
                    self._preventSleep()
            elif line == 'wake':
                self._restoreSleep()
            line = sys.stdin.readline().strip()


power_mixin(PowerProcess)

if __name__ == '__main__':
    p = PowerProcess()

    if sys.argv[1:]:
        if sys.argv[1] == 'test':
            p.start()
            import time
            p.preventSleep()
            time.sleep(10)
            p.restoreSleep()
            time.sleep(10)
            p.preventSleep('This is a message')
            time.sleep(10)
            p.restoreSleep()
            time.sleep(10)
        else:
            print('Usage: %s <test>' % (os.path.basename(__file__)))
    else:
        p.processCommands()
