"""Common cleanup"""


from pyats import aetest


class ScriptCommonCleanup(aetest.CommonCleanup):
    """define a common cleanup section by inherting from aetest"""

    @aetest.subsection
    def disconnect_from_devices(self):
        """Disconnect all devices"""
        pass
