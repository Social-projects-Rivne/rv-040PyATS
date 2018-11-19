# test.py
import os
from pyats import aetest


class Smoke(aetest.Testcase):

    @aetest.setup
    def create(self, directory):
        if not os.path.exists(directory):
            os.makedirs(directory)

    @aetest.test
    def foo(self, directory):
        with open('{directory}/foo.txt'.format(directory), 'w') as file:
            file.write('Some important info: foo')

    @aetest.test
    def bar(self, directory):
        with open('{directory}/bar.txt'.format(directory), 'w') as file:
            file.write('Some important info: bar')


if __name__ == '__main__':
    aetest.main()
