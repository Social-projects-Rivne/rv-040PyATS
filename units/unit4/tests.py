"""tests.py"""

import argparse
import sys
import os
from pyats import aetest


mapping = {'a': (1, 3, 4, 5, 6, 7, 8),
           'b': (0, 2, 3, 4),
           'c': (7, 9, 0, 6, 5, 4, 3, 1)}


def get_value():
    """return iterable list from mapping"""
    return mapping.get(os.environ['TEST_LETTER'])


class UnitTest(aetest.Testcase):
    """Main class for testing"""

    @aetest.setup
    def setup(self):
        """Setup"""
        # self.counter = 0
        # self.letter = letter

    @aetest.test.loop(number=get_value)
    def check(self, number):
        """Return one number from mapping by loop"""
        # self.counter += 1
        print('number: {}'.format(number))

    # @aetest.cleanup
    # def cleanup(self):
    #     """Cleanup"""
    #     assert len(get_value()) == self.counter


if __name__ == '__main__':
    # # parser arguments for command line
    # parser = argparse.ArgumentParser(description="Standalone parser")
    # parser.add_argument('--letter', type=str, default='a', required=False)
    # args, sys.argv[1:] = parser.parse_known_args(sys.argv[1:])
    # # run
    # aetest.main(letter=args.letter)
    aetest.main()