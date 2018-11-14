"""Tests for calculation.py"""

import argparse
import sys
from pyats import aetest

# sys.path.append('/home/class/ohrytsiuk/git/rv-040PyATS/')
sys.path.append('/home/grant/python/rv-040PyATS/')

from modules.calculation import add, divide


class UnitTest(aetest.Testcase):

    @aetest.setup
    def setup(self):
        """Setup"""
        pass

    @aetest.test
    def test_add(self, num1=3, num2=0):
        """Test calculation function add"""
        result = add(num1, num2)
        if result < 0:
            self.skipped("Result less than 0")
        assert result == sum((num1, num2))

    @aetest.test
    def test_divide(self, num1=3, num2=0):
        """Test calculation function divine"""
        try:
            result = divide(num1, num2)
            if result < 0:
                self.skipped("Result less than 0")
            assert result == num1 / num2
        except ZeroDivisionError:
            self.passx("Division by 0")

    @aetest.cleanup
    def cleanup(self):
        """Cleanup"""
        pass


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="standalone parser")
    parser.add_argument('-num1', type=int, required=False)
    parser.add_argument('-num2', type=int, required=False)

    # do the parsing
    # always use parse_known_args, as aetest needs to parse	any
    # remainder	arguments that this	parser does	not	understand
    args, sys.argv[1:] = parser.parse_known_args(sys.argv[1:])

    # and pass all arguments to aetest.main() as kwargs
    if args.num1 and args.num2:
        aetest.main(num1=args.num1, num2=args.num2)
    else:
        aetest.main()
