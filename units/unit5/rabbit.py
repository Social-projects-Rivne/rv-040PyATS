"""rabbit.py"""

from pyats import aetest


class InitTest(aetest.Testcase):
    """Main class for testing"""

    @aetest.setup
    def setup(self):
        """Setup before tests"""
        print("A setup of smoke test")

    @aetest.test
    def test_1(self, word):
        """Print word"""
        print(f'Test #1: {word}')

    @aetest.test
    def test_2(self, word):
        """Print word"""
        print(f'Test #2: {word}')

    @aetest.cleanup
    def cleanup(self):
        """CleanUp after tests"""
        print("A cleanup of smoke test")


# if __name__ == '__main__':
#     aetest.main(word='alongggggggggggggword')

# if __name__ == '__main__':
#     parser = argparse.ArgumentParser(description="Standalone parser")
#     parser.add_argument('-word', type=str, default='alongggggggggggggword', required=False)
#     args, sys.argv[1:] = parser.parse_known_args(sys.argv[1:])
#     aetest.main(word=args.word)
