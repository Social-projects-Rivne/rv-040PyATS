"""tests.py"""

import os
from pyats import aetest

from pyats.aetest import loader

PROJECT_DIR = os.path.dirname(__file__)


class InitTest(aetest.Testcase):
    """Main class for testing"""

    @aetest.setup
    def connect(self, testbed):
        self.vm = testbed.devices['vm']
        self.vm.connect(via='ssh', alias="second")


if __name__ == '__main__':
    # load testbase file
    testbed_file = loader.load(os.path.join(PROJECT_DIR, 'testbase.yaml'))
    # run
    aetest.main(testbed=testbed_file)