# rabbit.py
import argparse
import sys
import os
from pyats import aetest
from pyats.easypy import run


class SmokeTest(aetest.Testcase):

    @aetest.setup
    def setup(self):
        print("A setup of smoke test")

    @aetest.test
    def test_1(self, word):
        print('Test #1: {}'.format(word))

    @aetest.test
    def test_2(self, word):
        print('Test #2: {}'.format(word))

    @aetest.cleanup
    def cleanup(self):
        print("A cleanup of smoke test")


def main():
    parser = argparse.ArgumentParser(description="Standalone parser")
    parser.add_argument('-word', type=str, default='alongggggggggggggword', required=False)
    args, sys.argv[1:] = parser.parse_known_args(sys.argv[1:])
    run(testscript=os.path.dirname(__file__) + '/rabbit.py', word=args.word)
