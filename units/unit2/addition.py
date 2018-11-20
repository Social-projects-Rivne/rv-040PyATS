"""Addition test"""

from pyats import aetest


class UnitTest(aetest.Testcase):
    """Main class for addition testing"""

    @aetest.test
    def test_addition(self, num1, num2):
        """Test pass if addition > 0 another fail"""
        if num1 + num2 < 0:
            self.failed("Less than 0")
        self.passed("Test pass")


if __name__ == '__main__':
    aetest.main()
