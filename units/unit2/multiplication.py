"""Multiplication testing"""

from pyats import aetest


class UnitTest(aetest.Testcase):
    """Main class for multiplication testing"""

    @aetest.test
    def test_multiplication(self, num1, num2):
        """Test pass if multiplication > 0 another fail"""
        if num1 * num2 < 0:
            self.failed("Less than 0")
        self.passed("Test pass")
