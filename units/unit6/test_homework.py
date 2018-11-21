"""test_homework.py for testing"""

import os
from pyats import aetest

from pyats.topology import loader


class UnitTest(aetest.Testcase):
    """Main class for testing"""

    @aetest.setup
    def create(self, testbed):
        self._directory = testbed.custom.get('directory')
        if not os.path.exists(self._directory):
            os.makedirs(self._directory)

    @aetest.test
    def foo(self):
        """Print 1"""
        with open('{}/foo.txt'.format(self._directory), 'w') as file:
            file.write('Some important info: foo')

    @aetest.test
    def bar(self):
        """Print 2"""
        with open('{}/bar.txt'.format(self._directory), 'w') as file:
            file.write('Some important info: bar')


if __name__ == '__main__':
    # load testbase file
    testbed = loader.load(os.path.dirname(__file__) + '/testbase.yaml')
    # run
    aetest.main(testbed=testbed)
