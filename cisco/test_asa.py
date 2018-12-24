"""cisco asa"""

import os
from pyats import aetest

from genie.abstract import Lookup
from genie.conf import Genie
from genie.conf.base.config import CliConfig
from pyats.topology import loader
from genie.libs import ops
from genie.libs.ops.interface.iosxe.interface import Interface

PROJECT_DIR = os.path.dirname(__file__)


class UnitTest(aetest.Testcase):
    """Class for testing"""

    @aetest.setup
    def setup(self, testbed):
        """Set up and connect to devices and load config"""
        self.testbed = Genie.init(testbed)
        self.vm1 = self.testbed.devices['asa']
        # self.vm1.connect(via='a')
        # create config
        with open('big_config', 'w+') as file:
            for i in range(1000000):
                file.writelines("!Line " + str(i) + '\n')

    @aetest.cleanup
    def cleanup(self):
        """Clean up and disconnect from devices"""
        self.vm1.disconnect()


if __name__ == '__main__':
    # load testbase file
    testbed_file = loader.load(os.path.join(PROJECT_DIR, 'testbed.yaml'))
    # run
    aetest.main(testbed=testbed_file)
