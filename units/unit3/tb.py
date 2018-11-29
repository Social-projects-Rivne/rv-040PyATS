"""Tests for copy file between local and virtual machine"""

import os
from pyats import aetest

from pyats.topology import loader
from pyats.utils.fileutils.plugins.linux.fileutils import FileUtils

PROJECT_DIR = os.path.dirname(__file__)


class UnitTest(aetest.Testcase):
    """Class for testing"""

    @aetest.setup
    def setup(self, testbed):
        """Set up local and virtual source, destination folders"""
        # self.vm = testbed.devices['vm']
        # self.vm.connect(via='sftp', alias="second")
        self.local_source = testbed.custom.get('local_source')
        self.local_destination = testbed.custom.get('local_destination')
        self.remote_source = testbed.custom.get('remote_source')
        self.remote_destination = testbed.custom.get('remote_destination')

    @aetest.test
    def test_copy_from_pc(self, testbed):
        """Copy file from localhost to linux virtual machine using sftp"""
        with FileUtils(testbed=testbed) as futils:
            futils.copyfile(source=self.local_source,
                            destination=self.remote_destination,
                            timeout_seconds=120)
            # Check file on sftp server. If file exists return None else error
            assert futils.checkfile(self.remote_destination) is None

    @aetest.test
    def test_copy_from_vm(self, testbed):
        """Copy file from linux virtual machine to localhost using sftp"""
        with FileUtils(testbed=testbed) as futils:
            futils.copyfile(source=self.remote_source,
                            destination=self.local_destination,
                            timeout_seconds=120)
            # Check is file exists on local machine
            assert os.path.isfile(self.local_destination)

    @aetest.cleanup
    def cleanup(self, testbed):
        """Clean up test files from machines"""
        # self.vm.disconnect_all()
        # Delete test file from sftp server
        with FileUtils(testbed=testbed) as futils:
            futils.deletefile(target=self.remote_destination)
        # Delete test file from local machine
        os.remove(self.local_destination)


if __name__ == '__main__':
    # load testbase file
    testbed_file = loader.load(os.path.join(PROJECT_DIR, 'docker-env.yaml'))
    # run
    aetest.main(testbed=testbed_file)
