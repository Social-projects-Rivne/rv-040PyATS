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
            futils.copyfile(source='file:/home/class/ohrytsiuk/pyats/example.py',
                            destination='sftp://server_alias:2222/upload/123.py',
                            timeout_seconds=120)
            # assert futils.checkfile('sftp://server_alias:2222/upload/123.py') == None

    @aetest.test
    def test_copy_from_vm(self, testbed):
        """Copy file from linux virtual machine to localhost using sftp"""
        with FileUtils(testbed=testbed) as futils:
            futils.copyfile(source='sftp://server_alias:2222/upload/123.py',
                            destination='file:/home/class/ohrytsiuk/pyats/123.py',
                            timeout_seconds=120)
            # assert os.path.isfile('/home/class/ohrytsiuk/pyats/123.py123')

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
