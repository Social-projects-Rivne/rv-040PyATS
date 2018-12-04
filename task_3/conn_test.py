"""

Testing a connection to my vagrant machine, ping it and disconnect.
Run:  easypy conn_job.py -testbed_file testbed.yaml


"""
import os.path

from pyats import aetest
from pyats.aetest import test, setup, cleanup
from pyats.utils.fileutils import FileUtils


class Smoke(aetest.Testcase):

    @setup
    def connect(self, testbed):

        """Connect to remote machine"""
        self.vm = testbed.devices['DESKTOP-K0K4BRM']
        self.vm.connect()

        self.local_source = testbed.custom.get('local_source')
        self.local_destination = testbed.custom.get('local_destination')
        self.remote_source = testbed.custom.get('remote_source')
        self.remote_destination = testbed.custom.get('remote_destination')

    @test
    def test_copy_files_from_ssh(self, testbed):

        # copy file to local machine
        with FileUtils(testbed=testbed) as futils:
            futils.copyfile(
                source=self.remote_source,
                destination=self.local_destination,
                timeout_seconds=120
            )

        assert os.path.isfile(self.local_destination[7:] + 'Vagrantfile')

    @test
    def test_copy_files_to_ssh(self, testbed):

        # copy file to ssh vm
        with FileUtils(testbed=testbed) as futils:
            futils.copyfile(
                source=self.local_source,
                destination=self.remote_destination,
                timeout_seconds=120
            )

        assert futils.checkfile('sftp' + self.remote_destination[3:]) is None

    @cleanup
    def disconnect(self):
        self.vm.disconnect_all(exit())
