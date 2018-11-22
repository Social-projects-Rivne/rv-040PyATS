"""Testbed file for testing"""

import os
from pyats import aetest

from pyats.topology import loader
from pyats.utils.fileutils.plugins.linux.fileutils import FileUtils


class UnitTest(aetest.Testcase):
    """Class for testing"""

    @aetest.setup
    def connect(self, testbed):
        """Set up"""
        # self.vm = testbed.devices['vm']
        # self.vm.connect(via='sftp', alias="second")
        pass

    @aetest.test
    def test_copy_from_pc(self, testbed):
        """Copy file from localhost to linux virtual machine using sftp"""
        with FileUtils(testbed=testbed) as futils:
            futils.copyfile(source='file:/home/grant/python/123.py',
                            destination='sftp://server_alias:2222/upload/123.py',
                            timeout_seconds=120)
            # futils.checkfile(target='sftp://server_alias:2222/upload/123.py')
            assert futils.is_remote('sftp://server_alias:2222/upload/123.py')

    @aetest.test
    def test_copy_from_vm(self, testbed):
        """Copy file from linux virtual machine to localhost using sftp"""
        with FileUtils(testbed=testbed) as futils:
            futils.copyfile(source='sftp://server_alias:2222/upload/123.py',
                            destination='file:/home/grant/123.py',
                            timeout_seconds=120)
            assert futils.is_local('file:/home/grant/123.py')

    @aetest.cleanup
    def disconnect(self):
        """tear down"""
        # self.vm.disconnect_all()
        pass


if __name__ == '__main__':
    # load testbase file
    testbed = loader.load(os.path.dirname(__file__) + '/docker-env.yaml')
    # run
    aetest.main(testbed=testbed)
