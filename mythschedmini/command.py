from __future__ import print_function

import os
from multiprocessing import Process
from subprocess import Popen

from mythschedmini.mixins import power_mixin
from mythschedmini.powerprocess import PowerProcess

class CommandProcess(Process):
    def __init__(self, q):
        super(CommandProcess, self).__init__()
        self.q = q
        self.power_process = PowerProcess()
        self.power_process.start()

    def run(self):
        while True:
            func, params = self.q.get(True, None)

            if func == 'convert':
                cmd, directory = params
                if os.path.exists(os.path.join(directory, 'prog_index.m3u8')) or os.path.exists(os.path.join(directory, 'fileSequence0.ts')):
                    print('Already converted')
                else:
                    self.power_process.preventSleep("MythSchedMini.CommandProcess - preventing idle sleep")
                    p = Popen(cmd, shell=True)
                    p.wait()
                    # import time
                    # print(cmd)
                    # import time
                    # time.sleep(15)
                    # print('Done!')
                    self.power_process.restoreSleep()
            elif func == 'move':
                src, dest = params
                try:
                    os.renames(src, dest)
                except:
                    import traceback as tb
                    tb.print_exc()
            elif func == 'delete':
                pass

if __name__ == '__main__':
    from multiprocessing import Queue
    q = Queue()
    p = CommandProcess(q)
    p.start()
    q.put(('no command', 'no directory'))
    import time
    time.sleep(30)
    print('Done!')
