"""Tests for calculation.py"""

import argparse
import sys
from pyats import aetest

from pyats.utils.import_utils import import_from_name

add = import_from_name("calculation.add")
divide = import_from_name("calculation.divide")


class UnitTest(aetest.Testcase):
    """Main class for testing"""

    @aetest.test
    def test_add(self, num1, num2):
        """Test calculation function add"""
        result = add(num1, num2)
        if result < 0:
            self.skipped("Result less than 0")
        assert result == sum((num1, num2))

    @aetest.test
    def test_divide(self, num1, num2):
        """Test calculation function divine"""
        try:
            result = divide(num1, num2)
            if result < 0:
                self.skipped("Result less than 0")
            assert result == num1 / num2
        except ZeroDivisionError:
            self.passx("Division by 0")


if __name__ == '__main__':
    # parser arguments for command line
    parser = argparse.ArgumentParser(description="Standalone parser")
    parser.add_argument('-num1', type=int, default=3, required=False)
    parser.add_argument('-num2', type=int, default=0, required=False)
    args, sys.argv[1:] = parser.parse_known_args(sys.argv[1:])
    # run
    aetest.main(num1=args.num1, num2=args.num2)
