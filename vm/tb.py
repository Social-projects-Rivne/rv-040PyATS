
from pyats import aetest
from pyats.aetest import test, setup, cleanup
from pyats.topology import loader


class Smoke(aetest.Testcase):

    @setup
    def connect(self, testbed):
        self.vm = testbed.devices['vm']
        self.vm.connect()
        self.vm.connect(via='linux', alias="second")

    @test
    def test_one(self):
        self.vm.execute('hostname')
        self.vm.ping('108.177.119.103')
        self.vm.default.execute('hostname')
        self.vm.second.execute('hostname')

    @cleanup
    def	disconnect(self):
        self.vm.disconnect_all()


if __name__ == '__main__':
    testbed = loader.load('/home/class/ohrytsiuk/git/rv-040PyATS/vm/test-env.yaml')
    aetest.main(testbed=testbed)
