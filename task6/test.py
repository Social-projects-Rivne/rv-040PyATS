import os
from pyats import aetest

from pyats.topology import loader


class UnitTest(aetest.Testcase):
    """Main class for testing"""

    @aetest.setup
    def create(self, testbed):
        self.directory = testbed.custom.get('directory')
        # self.report_directory = testbed.custom.get('report_directory')
        if not os.path.exists(self.directory):
            os.makedirs(self.directory)
            # os.makedirs(self.report_directory)

    @aetest.test
    def foo(self):
        """Print 1"""
        with open('{}/foo.txt'.format(self.directory), 'w') as file:
            file.write('Some important info: foo')

    @aetest.test
    def bar(self):
        """Print 2"""
        with open('{}/bar.txt'.format(self.directory), 'w') as file:
            file.write('Some important info: bar')


if __name__ == '__main__':
    # load testbed file
    testbed = loader.load(os.path.dirname(__file__) + '/testbed.yaml')
    # run
    aetest.main(testbed=testbed)
