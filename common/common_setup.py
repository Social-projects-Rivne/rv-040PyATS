"""Common setup"""


from pyats import aetest


class ScriptCommonSetup(aetest.CommonSetup):
    """define a common setup section by inherting from aetest"""

    @aetest.subsection
    def connect_to_devices(self):
        """Connect to devices"""
        pass
