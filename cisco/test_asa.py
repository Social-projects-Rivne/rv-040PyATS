"""cisco asa"""

import os
from pyats import aetest

from genie.conf import Genie
from pyats.topology import loader

PROJECT_DIR = os.path.dirname(__file__)


class UnitTest(aetest.Testcase):
    """Class for testing"""

    @aetest.setup
    def setup(self, testbed):
        """Set up and connect to devices and load config"""
        self.testbed = Genie.init(testbed)
        self.vm1 = self.testbed.devices['asa']
        self.vm1.connect(via='a')
        with open('running-config', 'r') as file:
            config = file.read()
            self.vm1.configure(config)

    @aetest.cleanup
    def cleanup(self):
        """Clean up and disconnect from devices"""
        self.vm1.disconnect()


if __name__ == '__main__':
    # load testbase file
    testbed_file = loader.load(os.path.join(PROJECT_DIR, 'testbed.yaml'))
    # run
    aetest.main(testbed=testbed_file)
