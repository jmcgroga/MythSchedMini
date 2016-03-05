from __future__ import print_function

from mythschedmini.IOKit.pwr_mgt import *

def power_mixin(cls):
    def _preventSleep(self, msg = "MythSchedMini - preventing idle sleep"):
        retval = None

        if 'preventSleepAssertion' not in dir(self):
            self.preventSleepAssertion = None
        if not self.preventSleepAssertion:
            retval, self.preventSleepAssertion = IOPMAssertionCreateWithName(kIOPMAssertionTypePreventSystemSleep,
                                                                             kIOPMAssertionLevelOff,
                                                                             msg,
                                                                             None)
        return retval

    def _restoreSleep(self):
        print('_restoreSleep')
        if 'preventSleepAssertion' not in dir(self):
            self.preventSleepAssertion = None
        elif self.preventSleepAssertion is not None:
            IOPMAssertionRelease(self.preventSleepAssertion)            
            self.preventSleepAssertion = None

    cls._preventSleep = _preventSleep
    cls._restoreSleep = _restoreSleep
