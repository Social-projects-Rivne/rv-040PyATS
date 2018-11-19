"""
to run python test.py --letter <letter>

"""
import argparse
import sys
from pyats import aetest

mapping = {
    'a': (1,3,4,5,6,7,8),
    'b': (0,2,3,4),
    'c': (7,9,0,6,5,4,3,1)
}


def get_value():
    return mapping.get(args.letter)


class UnitTest(aetest.Testcase):
    """Main class for testing"""


    @aetest.test.loop(number=get_value)
    def check(self, number):
        print('number: {}'.format(number))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Standalone parser")
    parser.add_argument('--letter', type=str, default='a', required=False)
    args, sys.argv[1:] = parser.parse_known_args(sys.argv[1:])
    aetest.main(letter=args.letter)