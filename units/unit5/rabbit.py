"""rabbit.py"""

import argparse
import os
import sys
from pyats import aetest

from pyats.aetest import loader

PROJECT_DIR = os.path.dirname(__file__)


class InitTest(aetest.Testcase):
    """Main class for testing"""

    @aetest.setup
    def setup(self, testbed):
        """Setup before tests"""
        self.word = testbed.custom.get('word')
        print("A setup of unit test")

    @aetest.test
    def test_1(self):
        """Print word"""
        print('Test #1: {}'.format(self.word))

    @aetest.test
    def test_2(self):
        """Print word"""
        print('Test #2: {}'.format(self.word))

    @aetest.cleanup
    def cleanup(self):
        """CleanUp after tests"""
        print("A cleanup of unit test")


# if __name__ == '__main__':
#     # parser arguments for command line
#     parser = argparse.ArgumentParser(description="Standalone parser")
#     parser.add_argument('-word', type=str, default='alongggggggggggggword', required=False)
#     args, sys.argv[1:] = parser.parse_known_args(sys.argv[1:])
#     # run
#     aetest.main(word=args.word)

if __name__ == '__main__':
    # load testbase file
    testbed_file = loader.load(os.path.join(PROJECT_DIR, 'testbase.yaml'))
    # run
    aetest.main(testbed=testbed_file)