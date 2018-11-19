"""multiplication math operation"""

from pyats import aetest
from pyats.aetest import test


class multiplicationTest(aetest.Testcase):
    """multiplication math operation test if calculated result less than 0 test has to fail"""

    @test
    def multiplication(self, num1, num2):
        """multiplication math operation"""
        multiplication_result = num1 - num2
        assert multiplication_result >= 0, "multiplication_result should be >= 0"


if __name__ == '__main__':
    aetest.main()