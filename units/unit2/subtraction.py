"""Substraction test"""

from pyats import aetest


class UnitTest(aetest.Testcase):
    """Main class for substraction testing"""

    @aetest.test
    def test_subtraction(self, num1, num2):
        """Test pass if substraction > 0 another fail"""
        if num1 - num2 < 0:
            self.failed("Less than 0")
        self.passed("Test pass")
