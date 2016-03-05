from __future__ import print_function

import os
from time import time, ctime
from multiprocessing import Process
from multiprocessing import queues

from mythschedmini.mixins import power_mixin
from mythschedmini.powerprocess import PowerProcess

class PowerHandlerProcess(Process):
    def __init__(self, q, sleep_buffer = 300.0, queue_block_time = 5):
        super(PowerHandlerProcess, self).__init__()
        self.q = q
        self.sleep_buffer = sleep_buffer
        self.queue_block_time = queue_block_time
        self.preventSleepAssertion = None
        self.restoreSleepTime = None
        self.power_process = PowerProcess()
        self.power_process.start()

    def run(self):
        while True:
            try:
                duration = self.q.get(True, self.queue_block_time)
                self.preventSleep(duration)
                continue
            except queues.Empty:
                pass
            finally:
                self.restoreSleep()

    def preventSleep(self, duration):
        self.restoreSleepTime = time() + float(duration) + self.sleep_buffer
        print('Preventing sleep until:', ctime(self.restoreSleepTime))
        self.power_process.preventSleep("MythSchedMini.PowerHandlerProcess - preventing idle sleep")

    def restoreSleep(self):
        if self.restoreSleepTime and (time() > self.restoreSleepTime):
            print('Restoring idle sleep')
            self.power_process.restoreSleep()
            self.restoreSleepTime = None

if __name__ == '__main__':
    from multiprocessing import Queue
    q = Queue()
    p = PowerHandlerProcess(q, 10)
    p.start()
    q.put(10)
    import time
    time.sleep(30)
    print('Done!')
