"""cisco tests"""

import os
from pprint import pprint
from pyats import aetest

from genie.abstract import Lookup
from genie.conf import Genie
from genie.conf.base.config import CliConfig
from pyats.topology import loader
from genie.libs import ops
from genie.libs.ops.interface.nxos.interface import Interface

PROJECT_DIR = os.path.dirname(__file__)


class UnitTest(aetest.Testcase):
    """Class for testing"""

    @aetest.setup
    def setup(self):
        """Set up"""
        self.testbed = Genie.init('testbed.yaml')
        # self.vm1 = self.testbed.devices['Router1']
        # self.vm1.connect(via='a')
        # with open('c3745_startup-config.cfg', 'r') as file:
        #     config = file.read()
        #     self.vm1.configure(config)
        #     # CliConfig(device=self.vm1, unconfig=False, cli_config=config)
        #     # self.vm1.build_config()
        #
        # self.vm2 = self.testbed.devices['Router2']
        # self.vm2.connect(via='a')
        # with open('c3725_startup-config.cfg', 'r') as file:
        #     config = file.read()
        #     # CliConfig(device=self.vm2, unconfig=True, cli_config=config)
        #     # self.vm2.build_config()
        #     self.vm2.configure(config)


    @aetest.test
    def test(self):
        # print(self.vm1.ping('192.168.1.1'))
        print("olala")

        for name, device in self.testbed.devices.items():

            device.connect()
            abstract = Lookup.from_device(device)
            intf = abstract.ops.interface.interface.Interface(device)
            intf.learn()
            pprint(intf.info)

            for str_intf in intf.info:
                if intf.info[str_intf].get('oper_status', None) and intf.info[str_intf]['oper_status'] == 'up':
                    assert True
                else:
                    assert False

    @aetest.cleanup
    def cleanup(self, testbed):
        # self.vm1.disconnect()
        # self.vm2.disconnect()
        pass


if __name__ == '__main__':
    # load testbase file
    testbed_file = loader.load(os.path.join(PROJECT_DIR, 'testbed.yaml'))
    # run
    aetest.main(testbed=testbed_file)
