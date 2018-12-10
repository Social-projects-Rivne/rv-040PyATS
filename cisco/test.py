"""cisco tests"""

import os
from pyats import aetest

from pyats.topology import loader

PROJECT_DIR = os.path.dirname(__file__)


class UnitTest(aetest.Testcase):
    """Class for testing"""

    @aetest.setup
    def setup(self, testbed):
        """Set up"""
        self.vm1 = testbed.devices['c3745']
        self.vm1.connect(via='a', alias="second")
        self.vm1.second.execute('show clock')
        self.vm1.second.execute('ping 192.168.1.2')
        print("olala")


    @aetest.cleanup
    def cleanup(self, testbed):
        self.vm1.disconnect()


if __name__ == '__main__':
    # load testbase file
    testbed_file = loader.load(os.path.join(PROJECT_DIR, 'testbed.yaml'))
    # run
    aetest.main(testbed=testbed_file)
