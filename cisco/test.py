"""cisco tests"""

import os
# from pprint import pprint
from pyats import aetest
import logging

# from genie.abstract import Lookup
from genie.conf import Genie
import re
# from genie.conf.base.config import CliConfig
from pyats.topology import loader
from unicon.eal.expect import Spawn, TimeoutError
from unicon.eal.dialogs import Statement, Dialog
# from genie.libs import ops
# from genie.libs.ops.interface.iosxe.interface import Interface

PROJECT_DIR = os.path.dirname(__file__)


class UnitTest(aetest.Testcase):
    """Class for testing"""

    @aetest.setup
    def setup(self, testbed):
        """Set up"""
        self.testbed = Genie.init(testbed)
        self.vm1 = self.testbed.devices['c3745']
        self.vm1.connect(via='a')
        with open('c3745.cfg', 'r') as file:
            config = file.read()
            self.vm1.configure(config)

        self.vm2 = self.testbed.devices['c3725']
        self.vm2.connect(via='a')
        with open('c3725.cfg', 'r') as file:
            config = file.read()
            self.vm2.configure(config)

    @aetest.test
    def test_interfaces(self):
        interface_c3745 = self.vm1.execute("show ip int brief")
        ipv4_c3745 = interface_c3745.split("\r")[1]
        assert ipv4_c3745.split(' ')[12] == str(self.vm1.interfaces['FastEthernet0/0'].ipv4)[:-3]
        interface_c3725 = self.vm2.execute("show ip int brief")
        ipv4_c3725 = interface_c3725.split("\r")[1]
        assert ipv4_c3725.split(' ')[12] == str(self.vm2.interfaces['FastEthernet0/0'].ipv4)[:-3]

    @aetest.test
    def ping_one(self):
        destination = str(self.vm2.interfaces['FastEthernet0/0'].ipv4)[:-3]
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.INFO)

        try:
            result = self.vm1.ping(destination)

        except Exception as e:
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

    @aetest.test
    def ping_two(self):
        destination = str(self.vm1.interfaces['FastEthernet0/0'].ipv4)[:-3]
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.INFO)

        try:
            result = self.vm2.ping(destination)

        except Exception as e:
            self.failed('Ping {} from device {} failed with error: {}'.format(
                destination,
                self.vm2,
                str(e),
            ),
                goto=['exit'])
        else:
            match = re.search(r'Success rate is (?P<rate>\d+) percent', result)
            success_rate = match.group('rate')
            logger.info('Ping {} with success rate of {}%'.format(destination, success_rate))

    #  @aetest.cleanup
    # def cleanup(self):
    #     self.vm1.disconnect()
    #     self.vm2.disconnect()


if __name__ == '__main__':
    # load testbase file
    testbed_file = loader.load(os.path.join(PROJECT_DIR, 'testbed.yaml'))
    # run
    aetest.main(testbed=testbed_file)
