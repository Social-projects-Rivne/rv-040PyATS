"""

Testing a connection to my vagrant machine, ping it and disconnect.
Run:  easypy conn_job.py -testbed_file testbed.yaml

"""

from pyats import aetest
from pyats.topology import loader
from pyats.aetest import test, setup, cleanup
from pyats.utils.fileutils import FileUtils

class Smoke(aetest.Testcase):

    @setup
    def connect(self, testbed):
        self.vm = testbed.devices['DESKTOP-K0K4BRM']
        self.vm.connect()
        self.vm.connect(start="ssh vagrant@192.168.0.104")

    @test
    def test_one(self):
        self.vm.execute('DESKTOP-K0K4BRM')
        self.vm.ping('192.168.0.104')

    @test
    def test_copy_files_from_ssh(self):
        # copy file to local machile
        futils = FileUtils(testbed = testbed)
        futils.copyfile(
            source='scp://vagrant@192.169.0.104/home/vagrant/test/ssh',
            destination= '/home/a/Desktop/test/'
        )


    @test
    def test_copy_files_to_ssh(self):
        #copy file to ssh vm

        futils = FileUtils(testbed=testbed)
        futils.copyfile(
            source='/home/a/Desktop/test/ssh',
            destination='scp://vagrant@192.169.0.104/home/vagrant/test/'
            )

    @cleanup
    def disconnect(self):
        self.vm.disconnect_all(exit())


if __name__ == '__main__':
    testbed = loader.load('testbed.yaml')
    aetest.main(testbed=testbed)
