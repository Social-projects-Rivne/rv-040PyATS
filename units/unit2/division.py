"""Division test"""

from pyats import aetest


class UnitTest(aetest.Testcase):
    """Main class for division testing"""

    @aetest.test
    def test_division(self, num1, num2):
        """Test pass if division > 0 another fail or passx when division by 0"""
        try:
            result = num1 / num2
            if result < 0:
                self.failed("Less than 0")
            self.passed("Test pass")
        except ZeroDivisionError:
            self.passx("Division by 0")
