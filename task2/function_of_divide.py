from pyats import aetest


class UnitTest(aetest.Testcase):

    @aetest.test
    def test_division(self, num1, num2):
        try:
            result = num1 / num2
            if result < 0:
                self.failed("Less than 0")
            self.passed("Test pass")
        except ZeroDivisionError:
            self.passx("Division by 0")


if __name__ == '__main__':
    aetest.main()