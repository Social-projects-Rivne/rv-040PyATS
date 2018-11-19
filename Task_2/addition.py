"""addtion math operation"""

from pyats import aetest
from pyats.aetest import test


class AddtionTest(aetest.Testcase):
    """addtion math operation test if calculated result less than 0 test has to fail"""

    @test
    def addtion(self, num1, num2):
        """addtion math operation"""
        addition_result = num1 + num2
        assert addition_result >= 0, "addtion_result should be >= 0"


if __name__ == '__main__':
    aetest.main()