"""Common cleanup"""


from pyats import aetest


class ScriptCommonCleanup(aetest.CommonCleanup):
    # define a common cleanup section by inherting from aetest

    @aetest.subsection
    def remove_testbed_configurations(self):
        pass

    @aetest.subsection
    def disconnect_from_devices(self):
        pass
