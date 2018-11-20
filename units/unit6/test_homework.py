"""test_homework.py for testing"""

import os
from pyats import aetest

from pyats.topology import loader


class UnitTest(aetest.Testcase):
    """Main class for testing"""

    # @aetest.setup
    # def create(self, directory):
    #     if not os.path.exists(directory):
    #         os.makedirs(directory)

    @aetest.test
    def foo1(self):
        """Print 1"""
        # with open('{}/foo.txt'.format(directory), 'w') as file:
        #     file.write('Some important info: foo')
        print('1')

    @aetest.test
    def bar2(self):
        """Print 2"""
        # with open('{}/bar.txt'.format(directory), 'w') as file:
        #     file.write('Some important info: bar')
        print('2')


if __name__ == '__main__':
    # load testbase file
    testbed = loader.load(os.path.dirname(__file__) + '/testbase.yaml')
    # run
    aetest.main(testbed=testbed)
