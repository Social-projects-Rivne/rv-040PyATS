"""cisco tests"""

import os
from pyats import aetest

from pyats.topology import loader
from unicon.eal.dialogs import Dialog

PROJECT_DIR = os.path.dirname(__file__)


class UnitTest(aetest.Testcase):
    """Class for testing"""

    @aetest.setup
    def setup(self, testbed):
        """Set up"""
        self.vm1 = testbed.devices['c3745']
        self.vm1.connect(via='a')
        # self.vm1.second.execute('show clock')
        # self.vm1.second.execute('ping 192.168.1.2')
        # self.vm1.second.execute('show ip int brief')
        with open('c3745_startup-config.cfg', 'r') as file:
            config = file.read()
            self.vm1.send('config t')
            for cmd_str in config.splitlines():
                self.vm1.execute(cmd_str)
            self.vm1.send('end')
            # dialog = Dialog([[r"^confirm", lambda spawn: spawn.sendline("yes"), None, True, False]])
            # self.vm1.configure(config, timeout=10)
        print("olala")


    @aetest.cleanup
    def cleanup(self, testbed):
        self.vm1.disconnect()


if __name__ == '__main__':
    # load testbase file
    testbed_file = loader.load(os.path.join(PROJECT_DIR, 'testbed.yaml'))
    # run
    aetest.main(testbed=testbed_file)
