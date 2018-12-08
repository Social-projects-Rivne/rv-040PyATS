"""Test file"""

import os
from pyats import aetest

from pyats.topology import loader
from pyats.utils.fileutils.plugins.linux.fileutils import FileUtils


class UnitTest(aetest.Testcase):
    """Class for testing"""


    @aetest.test
    def connect_vm(self, testbed):

        self.device = testbed.devices['vm']
        self.device.connect()
        self.device.execute('show ip int brief')
        self.device.execute('ping 192.168.1.1')


    @aetest.cleanup
    def disconect(self):
        self.device.disconnect()


if __name__ == '__main__':
    testbed = loader.load(os.path.dirname(__file__) + '/testbed.yaml')
    aetest.main(testbed=testbed)