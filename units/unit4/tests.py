"""Looping tests for list"""

import argparse
import sys
from pyats import aetest


MAPPING = {'a': (1, 3, 4, 5, 6, 7, 8),
           'b': (0, 2, 3, 4),
           'c': (7, 9, 0, 6, 5, 4, 3, 1)}


def get_value():
    """return iterable list from mapping"""
    return MAPPING.get(args.letter)


class UnitTest(aetest.Testcase):
    """Main class for testing"""

    @aetest.test.loop(number=get_value)
    def check(self, number):
        """Return one number from mapping by loop"""
        print('number: {}'.format(number))


if __name__ == '__main__':
    # parser arguments for command line
    parser = argparse.ArgumentParser(description="Standalone parser")
    parser.add_argument('--letter', type=str, default='a', required=False)
    args, sys.argv[1:] = parser.parse_known_args(sys.argv[1:])
    # run
    aetest.main(letter=args.letter)
