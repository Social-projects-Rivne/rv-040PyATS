# Example
# -------
#
#   an example common cleanup

# import the aetest module

from pyats import aetest


# define a common cleanup section by inherting from aetest
class ScriptCommonCleanup(aetest.CommonCleanup):

    @aetest.subsection
    def remove_testbed_configurations(self):
        pass

    @aetest.subsection
    def disconnect_from_devices(self):
        pass
