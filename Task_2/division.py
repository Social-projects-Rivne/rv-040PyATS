"""division math operation"""


from pyats import aetest
from pyats.aetest import test


class DivisionTest(aetest.Testcase):
    """division math operation test if calculated result less than 0 test has to fail"""


    @test
    def division(self, num1, num2):
        """division math operation"""

        try:
            division_result = num1 / num2
            assert division_result >= 0, "division_result should be >= 0"
        except ZeroDivisionError:
            self.failed('Division by zero')


if __name__ == '__main__':
    aetest.main()