"""cisco tests"""

import os
import re
from pprint import pprint
from pyats import aetest

from genie.abstract import Lookup
from genie.conf import Genie
from genie.libs import ops
from pyats.topology import loader


PROJECT_DIR = os.path.dirname(__file__)


class UnitTest(aetest.Testcase):
    """Class for testing"""

    @aetest.setup
    def setup(self):
        """Set up"""
        self.testbed = Genie.init('testbed.yaml')

        self.vm1 = self.testbed.devices['Router1']
        self.vm1.connect(via='a')
        with open('c3745_startup-config.cfg', 'r') as file:
            config = file.read()
            self.vm1.configure(config)


        self.vm2 = self.testbed.devices['Router2']
        self.vm2.connect(via='a')
        with open('c3725_startup-config.cfg', 'r') as file:
            configs = file.read()
            self.vm2.configure(configs)



    @aetest.test
    def test_routers_configuration(self):
        """test if devices is configured"""

        #check Router1
        interface_Rounter1 = self.vm1.execute("show ip int brief | section 2")
        assert interface_Rounter1.split()[1] == str(self.vm1.interfaces['FastEthernet0/0'].ipv4)[:-3]

        #check Router2
        interface_Rounter2 = self.vm2.execute("show ip int brief | section 2")
        assert interface_Rounter2.split()[1] == str(self.vm2.interfaces['FastEthernet0/0'].ipv4)[:-3]




    @aetest.cleanup
    def cleanup(self):
        self.vm1.disconnect()
        self.vm2.disconnect()


if __name__ == '__main__':
    # load testbase file
    testbed_file = loader.load(os.path.join(PROJECT_DIR, 'testbed.yaml'))
    # run
    aetest.main(testbed=testbed_file)
