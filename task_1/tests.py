"""to run: python task_1/tests.py -num1 <arg> -num2 <arg>"""

import argparse
import sys

from pyats import aetest
from pyats.utils.import_utils import import_from_name
from pyats.aetest import test, setup, cleanup

add = import_from_name('calculation.add')
divide = import_from_name('calculation.divide')

parameters = {
    'num1': 3,
    'num2': 0

}


class SmokeTest(aetest.Testcase):

    @setup
    def setup(self):
        pass

    @test
    def test_add(self, num1, num2):

        """Test add"""
        result = add(num1, num2)

        if result < 0:
            self.skipped("Result < 0")
        else:
            assert result == num1 + num2

    @test
    def test_divide(self, num1, num2):

        """Test divide"""
        try:
            result = divide(num1, num2)
            if result < 0:
                self.skipped("Result less than 0")
            assert result == num1 / num2
        except ZeroDivisionError:
            self.passx("Division by 0")

    @cleanup
    def cleanup(self):
        """Cleanup"""
        pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="standalone parser")
    parser.add_argument('-num1', type=int, required=False)
    parser.add_argument('-num2', type=int, required=False)
    args, sys.argv[1:] = parser.parse_known_args(sys.argv[1:])

    if args.num1 is not None and args.num2 is not None:
        aetest.main(num1=args.num1, num2=args.num2)
    else:
        aetest.main()
