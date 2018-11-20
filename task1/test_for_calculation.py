import argparse
from pyats import aetest
from pyats.aetest import setup, test, cleanup
from calculation import add, divide


class UnitTest(aetest.Testcase):

    @setup
    def setup(self):
        """Setup"""
        pass

    @test
    def test_add(self, num1, num2):
        """Test calculation function add"""
        result = add(num1, num2)
        if result < 0:
            self.skipped("Result less than 0")
        assert result == sum((num1, num2))

    @test
    def test_divide(self, num1, num2):
        """Test calculation function divide"""
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


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Standalone parser")
    parser.add_argument("num1", nargs='?', default=3, type=int)
    parser.add_argument("num2", nargs='?', default=0, type=int)
    args = parser.parse_args()
    aetest.main(num1=args.num1, num2=args.num2)
