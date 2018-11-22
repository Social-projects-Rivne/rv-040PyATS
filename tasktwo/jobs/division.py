from pyats import aetest


class UnitTest(aetest.Testcase):

    @aetest.test
    def test_division(self, num1, num2):
        try:
            result = num1 / num2
            if result < 0:
                self.failed("Result < 0")
            self.passed("Test pass")
        except ZeroDivisionError:
            self.passx("num2 = 0")


if __name__ == '__main__':
    aetest.main()
