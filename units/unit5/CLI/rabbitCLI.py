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
    def setup(self):
        """Setup before tests"""
        print("A setup of unit test")

    @aetest.test
    def test_1(self, word):
        """Print word"""
        print('Test #1: {}'.format(word))

    @aetest.test
    def test_2(self, word):
        """Print word"""
        print('Test #2: {}'.format(word))

    @aetest.cleanup
    def cleanup(self):
        """CleanUp after tests"""
        print("A cleanup of unit test")
