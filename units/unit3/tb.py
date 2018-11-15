"""Testbed file for testing"""

from pyats import aetest
from pyats.topology import loader
from pyats.utils.fileutils import FileUtils


class UnitTest(aetest.Testcase):

    # @aetest.setup
    # def connect(self, testbed):
    #     self.vm = testbed.devices['vm']
    #     self.vm.connect()
    #     self.vm.connect(via='linux', alias="second")

    # @aetest.test
    # def test_one(self):
    #     self.vm.execute('hostname')
    #     self.vm.ping('8.8.8.8')
    #     self.vm.default.execute('hostname')
    #     self.vm.second.execute('hostname')

    # @aetest.test
    # def test_copy_from_vm(self, testbed):
    #     futils = FileUtils.from_device(testbed.devices['vm'])

    @aetest.test
    def test_copy_from_pc(self, testbed):
        futils = FileUtils(testbed=testbed.devices['vm'])
        futils.copyfile(source='file:/home/grant/python/rv-040PyATS/units/unit3/readme.md',
                        destination='sftp://localhost/upload',
                        timeout_seconds=120)

    # @aetest.cleanup
    # def disconnect(self):
    #     self.vm.disconnect_all()


if __name__ == '__main__':
    testbed = loader.load('docker-env.yaml')
    aetest.main(testbed=testbed)
