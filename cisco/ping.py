"""cisco tests"""

import logging
import os
import re

from pyats import aetest
from genie.conf import Genie
from pyats.topology import loader
from unicon.core.errors import SubCommandFailure

PROJECT_DIR = os.path.dirname(__file__)


class UnitTest(aetest.Testcase):
    """Class for testing"""

    @aetest.setup
    def setup(self):
        """Configuring routers"""
        self.testbed = Genie.init('testbed.yaml')
        self.vm1 = self.testbed.devices['Router1']
        self.vm1.connect(via='a')
        with open('3745_1.cfg', 'r') as file:
            config = file.read()
            self.vm1.configure(config)


        self.vm2 = self.testbed.devices['Router2']
        self.vm2.connect(via='a')
        with open('r2.cfg', 'r') as file:
            config = file.read()
            self.vm2.configure(config)

    @aetest.test
    def test(self):
        """Ping"""

        destination = str(self.vm2.interfaces['FastEthernet0/0'].ipv4)[:-3]
        # destination = '192.168.1.5'
        logger = logging.getLogger(__name__)

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


    @aetest.cleanup
    def cleanup(self):
        """Disconnect"""
        self.vm1.disconnect()
        self.vm2.disconnect()


if __name__ == '__main__':
    # load testbase file
    testbed_file = loader.load(os.path.join(PROJECT_DIR, 'testbed.yaml'))
    # run
    aetest.main(testbed=testbed_file)
