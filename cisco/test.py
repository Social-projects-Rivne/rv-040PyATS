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
        """Set up"""
        self.testbed = Genie.init(testbed)
        self.vm1 = self.testbed.devices['c3745']
        self.vm1.connect(via='a')
        # with open('c3745_startup-config.cfg', 'r') as file:
        #     config = file.read()
        #     self.vm1.configure(config)
        #     # CliConfig(device=self.vm1, unconfig=False, cli_config=config)
        #     # self.vm1.build_config()

        self.vm2 = self.testbed.devices['c3725']
        self.vm2.connect(via='a')
        # with open('c3725_startup-config.cfg', 'r') as file:
        #     config = file.read()
        #     # CliConfig(device=self.vm2, unconfig=True, cli_config=config)
        #     # self.vm2.build_config()
        #     self.vm2.configure(config)

    @aetest.test
    def test(self):

        interfaces = Interface(device=self.vm1)
        interfaces.learn()
        # pprint(intf1.info)

        for interface, value in interfaces.info.items():
            if interface in self.vm1.interfaces:
                pass

        links = self.vm1.find_links(self.vm2)

        # abstract1 = Lookup.from_device(self.vm1)
        # intf1 = abstract1.ops.interface.interface.Interface(self.vm1)
        # intf1.learn()
        # pprint(intf1.info)

        # with open('c3745', 'wb') as f:
        #     f.write(intf1.pickle())

        # abstract2 = Lookup.from_device(self.vm2)
        # intf2 = abstract2.ops.interface.interface.Interface(self.vm2)
        # intf2.learn()
        # pprint(intf2.info)
        # # with open('c3725', 'wb') as f:
        # #     f.write(intf2.pickle())

        # result1 = self.vm1.execute('show version')

        # # print(self.vm1.ping('192.168.1.1'))
        # print("olala")
        #
        # for name, device in self.testbed.devices.items():
        #
        #     device.connect()
        #     abstract = Lookup.from_device(device)
        #     intf = abstract.ops.interface.interface.Interface(device)
        #     intf.learn()
        #     pprint(intf.info)
        #
        #     for str_intf in intf.info:
        #         if intf.info[str_intf].get('oper_status', None) and intf.info[str_intf]['oper_status'] == 'up':
        #             assert True
        #         else:
        #             assert False

    @aetest.cleanup
    def cleanup(self, testbed):
        self.vm1.disconnect()
        self.vm2.disconnect()


if __name__ == '__main__':
    # load testbase file
    testbed_file = loader.load(os.path.join(PROJECT_DIR, 'testbed.yaml'))
    # run
    aetest.main(testbed=testbed_file)
