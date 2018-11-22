from pyats import aetest


class UnitTest(aetest.Testcase):

    @aetest.test
    def test_addition(self, num1, num2):
        result = num1 + num2
        if result < 0:
            self.failed("Result < 0")
        self.passed("Test pass")


if __name__ == '__main__':
    aetest.main()
