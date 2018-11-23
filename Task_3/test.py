"""Test file"""

import os
from pyats import aetest

from pyats.topology import loader
from pyats.utils.fileutils.plugins.linux.fileutils import FileUtils


class UnitTest(aetest.Testcase):
    """Class for testing"""


    @aetest.test
    def test_copy_from_pc(self, testbed):
        """Copy file from localhost to linux virtual machine using sftp"""
        with FileUtils(testbed=testbed) as futils:
            futils.copyfile(source='file:/home/shepsel/Downloads/staff/pyats-06.pdf',
                            destination='sftp://server_alias:2222/upload/pyats-06.pdf',
                            timeout_seconds=60)
            assert futils.checkfile('sftp://server_alias:2222/upload/pyats-06.pdf') == None

    @aetest.test
    def test_copy_from_vm(self, testbed):
        """Copy file from linux virtual machine to localhost using sftp"""
        with FileUtils(testbed=testbed) as futils:
            futils.copyfile(source='sftp://server_alias:2222/upload/pyats-06.pdf',
                            destination='file:/home/shepsel/Downloads/staff/fromserver/pyats-06.pdf',
                            timeout_seconds=60)
            assert os.path.isfile('/home/shepsel/Downloads/staff/fromserver/pyats-06.pdf')


# if __name__ == '__main__':
#     testbed = loader.load(os.path.dirname(__file__) + '/docker-env.yaml')
#     aetest.main(testbed=testbed)