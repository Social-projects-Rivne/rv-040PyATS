"""test.py for testing. Create txt files and write some info"""

import os
from pyats import aetest

from pyats.topology import loader

PROJECT_DIR = os.path.dirname(__file__)


class UnitTest(aetest.Testcase):
    """Main class for testing"""

    @aetest.setup
    def create(self, testbed):
        """Create directory from testbed file if it don't exist"""
        self._directory = testbed.custom.get('directory')
        if not os.path.exists(self._directory):
            os.makedirs(self._directory)

    @aetest.test
    def spam(self):
        """Write some info into txt file"""
        with open('{}/foo.txt'.format(self._directory), 'w') as file:
            file.write('Some important info: foo')

    @aetest.test
    def eggs(self):
        """Write some info into txt file"""
        with open('{}/bar.txt'.format(self._directory), 'w') as file:
            file.write('Some important info: bar')


if __name__ == '__main__':
    # load testbase file
    testbed_file = loader.load(os.path.join(PROJECT_DIR, 'testbase.yaml'))
    # run
    aetest.main(testbed=testbed_file)
