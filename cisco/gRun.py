# # Import Genie run
# import os
#
# from genie.harness.main import gRun
#
# PROJECT_DIR = os.path.dirname(__file__)
#
#
# def main():
#     # Set job file path to current directory
#     # gRun(mapping_datafile=os.path.join(PROJECT_DIR, 'mapping.yaml'),
#     #      runtime=runtime, config_datafile=os.path.join(PROJECT_DIR, 'configs.yaml'))
#     gRun(config_datafile=os.path.join(PROJECT_DIR, 'configs.yaml'))

from genie.conf import Genie
from genie.conf.base import Interface

# Load Genie testbed
testbed = Genie.init(testbed='testbed.yaml')
uut = testbed.devices['c3745']
uut.connect()
# Create an NXOS interface
nxos_interface = Interface(device=uut, name='Ethernet0/1')
# Add some configuration
nxos_interface.ipv4 = '192.168.1.1'
nxos_interface.ipv4.netmask ='255.255.255.0'
nxos_interface.switchport_enable = False
nxos_interface.shutdown = False
# Verify configuration generated
print("VASASA")
print(nxos_interface.build_config(apply=False))
print("VASASASA")
# interface Ethernet4/3
#  no shutdown
#  no switchport
#  ip address 200.1.1.2 255.255.255.0
#  exit
nxos_interface.build_config() # To apply on the device
nxos_interface.build_unconfig() # To remove configuration