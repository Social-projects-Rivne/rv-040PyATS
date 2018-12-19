"""Cisco virtual network configuration and tests"""

import logging
import os
import re

from pyats import aetest
from genie.abstract import Lookup
from genie.conf import Genie
from genie.libs import ops
from pyats.aetest import test, setup, cleanup
from pyats.topology import loader

from unicon.core.errors import SubCommandFailure


PROJECT_DIR = os.path.dirname(__file__)


class UnitTest(aetest.Testcase):
    """Class for testing"""

    @setup
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

    @test
    def test_routers_configuration(self):
        """Test if devices are configured"""


        #check Router1
        try:
            interface_router1 = self.vm1.execute("show ip int brief | section 2")
            assert interface_router1.split()[1] == str(self.vm1.interfaces['FastEthernet0/0'].ipv4)[:-3]

        except AssertionError:
            self.failed("Wrong ip on Router 1. Bad configuration")

        #check Router2
        try:
            interface_router2 = self.vm2.execute("show ip int brief | section 2")
            assert interface_router2.split()[1] == str(self.vm2.interfaces['FastEthernet0/0'].ipv4)[:-3]

        except AssertionError:
            self.failed("Wrong ip on Router 2. Bad configuration")

    @test
    def test_ping_btw_routers(self):
        """Test ping between routers. To check if they have link"""

        logger = logging.getLogger(__name__)

        destination = str(self.vm2.interfaces['FastEthernet0/0'].ipv4)[:-3]

        try:
            result = self.vm1.ping(destination)

        except SubCommandFailure as e:
            self.failed('Ping {} from device {} failed with error: {}'.format(
                destination,
                self.vm1,
                str(e),
            ),
                goto=['exit'])
        else:
            match = re.search(r'Success rate is (?P<rate>\d+) percent', result)
            success_rate = match.group('rate')

            logger.info('Ping {} with success rate of {}%'.format(destination, success_rate))

    # @cleanup
    # def cleanup(self):
    #     self.vm1.disconnect()
    #     self.vm2.disconnect()


if __name__ == '__main__':
    # load testbase file
    testbed_file = loader.load(os.path.join(PROJECT_DIR, 'testbed.yaml'))
    # run
    aetest.main(testbed=testbed_file)
