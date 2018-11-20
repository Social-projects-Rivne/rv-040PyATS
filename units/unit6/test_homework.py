# test.py

import os
from pyats import aetest

from pyats.easypy.plugins.bases import BasePlugin
from pyats.topology import loader


class UnitTest(aetest.Testcase):

    # @aetest.setup
    # def create(self, directory):
    #     if not os.path.exists(directory):
    #         os.makedirs(directory)

    @aetest.test
    def foo(self):
        # with open('{}/foo.txt'.format(directory), 'w') as file:
        #     file.write('Some important info: foo')
        print('1')

    @aetest.test
    def bar(self):
        # with open('{}/bar.txt'.format(directory), 'w') as file:
        #     file.write('Some important info: bar')
        print('2')


if __name__ == '__main__':
    # testbed = loader.load(os.path.dirname(__file__) + '/testbase.yaml')
    # aetest.main(testbed=testbed)
    BasePlugin.run()

