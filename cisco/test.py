"""cisco tests"""

import os
from pprint import pprint
from pyats import aetest

from genie.abstract import Lookup
from genie.conf import Genie
from genie.conf.base.config import CliConfig
from pyats.topology import loader
from genie.libs import ops
from genie.libs.ops.interface.iosxe.interface import Interface

PROJECT_DIR = os.path.dirname(__file__)


class UnitTest(aetest.Testcase):
    """Class for testing"""

    @aetest.setup
    def setup(self, testbed):
        """Set up and connect to devices and load config"""
        self.testbed = Genie.init(testbed)
        self.vm1 = self.testbed.devices['c3745']
        self.vm1.connect(via='a')
        with open('c3745', 'r') as file:
            config = file.read()
            self.vm1.configure(config)
            # CliConfig(device=self.vm1, unconfig=False, cli_config=config)
            # self.vm1.build_config()

        self.vm2 = self.testbed.devices['c3725']
        self.vm2.connect(via='a')
        with open('c3725', 'r') as file:
            config = file.read()
            self.vm2.configure(config)
            # CliConfig(device=self.vm2, unconfig=True, cli_config=config)
            # self.vm2.build_config()

    def interfaces(self, ints):
        """Method for verifying interfaces"""
        try:
            if ints.device.alias is self.vm1.alias:
                for interface, value in ints.info.items():
                    if interface in self.vm1.interfaces:
                        assert str(self.vm1.interfaces[interface].ipv4.ip) in str(value.get('ipv4').keys())
            elif ints.device.alias is self.vm2.alias:
                for interface, value in ints.info.items():
                    if interface in self.vm2.interfaces:
                        assert str(self.vm2.interfaces[interface].ipv4.ip) in str(value.get('ipv4').keys())
        except KeyError:
            assert False

    @aetest.test
    def verify_interfaces(self):
        """verify interfaces from config and device"""

        interfaces_vm1 = Interface(device=self.vm1)
        interfaces_vm1.learn()
        interfaces_vm1.learn_poll(verify=self.interfaces, sleep=30, attempt=5)

        interfaces_vm2 = Interface(device=self.vm2)
        interfaces_vm2.learn()
        interfaces_vm2.learn_poll(verify=self.interfaces, sleep=30, attempt=5)

        # links = self.vm1.find_links(self.vm2)

        # abstract1 = Lookup.from_device(self.vm1)
        # intf1 = abstract1.ops.interface.interface.Interface(self.vm1)
        # intf1.learn()
        # pprint(intf1.info)

    @aetest.test
    def ping_ftp(self):
        """ping test tftp server"""

        try:
            assert self.vm1.ping(self.testbed.servers.tftp.get('address'))
            assert self.vm2.ping(self.testbed.servers.tftp.get('address'))
        except Exception:
            assert False

    @aetest.cleanup
    def cleanup(self):
        """Clean up and disconnect from devices"""
        self.vm1.disconnect()
        self.vm2.disconnect()


if __name__ == '__main__':
    # load testbase file
    testbed_file = loader.load(os.path.join(PROJECT_DIR, 'testbed.yaml'))
    # run
    aetest.main(testbed=testbed_file)
