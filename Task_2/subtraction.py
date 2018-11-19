"""addition math operation"""

from pyats import aetest
from pyats.aetest import test


class SubtractionTest(aetest.Testcase):
    """addition math operation test if calculated result less than 0 test has to fail"""

    @test
    def addition(self, num1, num2):
        """addition math operation"""
        addition_result = num1 - num2
        assert addition_result >= 0, "addition_result should be >= 0"


if __name__ == '__main__':
    aetest.main()