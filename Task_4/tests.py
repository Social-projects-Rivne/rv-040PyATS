"""test with looping
comand for run - python <path to>/tests.py --letter <a or b or c>
"""


import argparse
import sys


from pyats import aetest


mapping = {
'a': (1,3,4,5,6,7,8),
'b': (0,2,3,4),
'c': (7,9,0,6,5,4,3,1),
}


def get_values():
    return mapping.get(args.letter)
    # return mapping[args.letter]

class Test(aetest.Testcase):

    @aetest.setup
    def setup(self, letter):
        pass


    @aetest.test.loop(number=get_values)
    def check(self, number):
        print(f'number: {number}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="standalone parser")
    parser.add_argument('--letter',  type=str, default='a', required=False)
    args, sys.argv[1:] = parser.parse_known_args(sys.argv[1:])
    aetest.main(letter=args.letter)