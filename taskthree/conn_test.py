"""

Testing a connection to my vagrant machine, ping it and disconnect.
Run:  easypy conn_job.py -testbed_file testbed.yaml


"""

from pyats import aetest
from pyats.topology import loader
from pyats.aetest import test, setup, cleanup
from pyats.utils.fileutils import FileUtils

testbed = loader.load('testbed.yaml')


class Smoke(aetest.Testcase):

    @setup
    def connect(self):
        self.vm = testbed.devices['DESKTOP-K0K4BRM']
        self.vm.connect()
        self.vm.connect(start="ssh vagrant@192.169.0.104")

    @test
    def test_one(self):
        self.vm.execute('DESKTOP-K0K4BRM')
        self.vm.ping('192.169.0.104')

    @test
    def test_copy_files_from_ssh(self):
        # copy file to local machile

        with FileUtils(testbed=testbed) as futils:
            futils.copyfile(
                source='scp://192.169.0.104/home/vagrant/test/Vagrantfile',
                destination='file:///home/class/selen/rv-040PyATS/taskthree/copy/',
                timeout_seconds=120
            )

    @test
    def test_copy_files_to_ssh(self):
        #copy file to ssh vm

        with FileUtils(testbed=testbed) as futils:
            futils.copyfile(
                source='file:///home/class/selen/rv-040PyATS/taskthree/copy/Vagrantfile',
                destination='scp://192.169.0.104/home/vagrant/test/',
                timeout_seconds=120
            )

    @cleanup
    def disconnect(self):
        self.vm.disconnect_all(exit())


if __name__ == '__main__':
    aetest.main(testbed=testbed)
