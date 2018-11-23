"""Tests for calculation.py
python tests_calculation.py -num1 <argument> -num2 <argument> - comand to start test
"""
import argparse
import sys

from pyats import aetest
from pyats.aetest import test
from calculation import add, divide


class CalculationTestCase(aetest.Testcase):
    """Calculation test case"""


    @test
    def test_sum(self, num1, num2):
        """Testing of adding num1 and num2"""
        if add(num1, num2) < 0:
            self.skipped('calculated value < 0')
        suma = num2+num1
        assert add(num1, num2) == suma, ' num1+num2 != num1+num2'


    @test
    def test_divide(self, num1, num2):
        """Testing of dividing num1 by num2"""
        try:
            division_value = num1 / num2
            if divide(num1, num2) < 0:
                self.skipped("calculated value < 0")
            assert divide(num1, num2) == division_value, 'num1/num2 != num1/num2'
        except ZeroDivisionError:
            self.passx('Division by zero')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="standalone parser")
    parser.add_argument('-num1',  type=int, default=3, required=False)
    parser.add_argument('-num2',  type=int, default=0, required=False)
    # do the parsing
    # always use parse_known_args, as aetest needs to parse any
    # remainder arguments that this parser does not understand
    args, sys.argv[1:] = parser.parse_known_args(sys.argv[1:])
    # and pass all arguments to aetest.main() as kwargs
    aetest.main(num1=args.num1, num2=args.num2)

