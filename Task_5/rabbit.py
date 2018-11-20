import argparse
import sys

from pyats import aetest
from pyats.aetest import setup, test, cleanup


class SmokeTest(aetest.Testcase):


    @setup
    def setup(self):
        print("A setup of smoke test")


    @test
    def test_1(self, word):
        print(f'Test #1: {word}')


    @test
    def test_2(self, word):
        print(f'Test #2: {word}')


    @cleanup
    def cleanup(self):
        print("A cleanup of smoke test")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="standalone parser")
    parser.add_argument('-word', type=str, default='alongggggggggggggword', required=False)
    args, sys.argv[1:] = parser.parse_known_args(sys.argv[1:])
    aetest.main(word=args.word)