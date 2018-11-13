"""calculation.py"""
import argparse
import sys
from pyats import aetest

import sys
sys.path.append('/home/class/ohrytsiuk/git/rv-040PyATS/calculation')

from calculation import add, divide


class UnitTest(aetest.Testcase):

    @aetest.setup
    def setup(self):
        pass

    @aetest.test
    def	test_add(self, num1=3, num2=0):
        result = add(num1, num2)
        assert result == sum((num1, num2))

    @aetest.test
    def test_divide(self, num1=3, num2=0):
        try:
            result = divide(num1, num2)
            assert result == num1 / num2
        except ZeroDivisionError:
            self.passx("Division by 0")

    @aetest.cleanup
    def cleanup(self):
        pass


if __name__	== '__main__':
    # num1 = input("Number 1: ")
    # num2 = input("Number 2: ")
    # if num1 and num2:
    #     aetest.main(num1=int(num1), num2=int(num2))
    # else:
    #     aetest.main()

    parser = argparse.ArgumentParser(description="standalone parser")
    parser.add_argument('-num1', type=int, required=True)
    parser.add_argument('-num2', type=int, required=True)

    #	do	the	parsing
    #	always	use	parse_known_args,	as	aetest	needs	to	parse	any
    #	remainder	arguments	that	this	parser	does	not	understand
    args, sys.argv[1:] = parser.parse_known_args(sys.argv[1:])

    #	and	pass	all	arguments	to	aetest.main()	as	kwargs
    aetest.main(num1=args.num1, num2=args.num2)
