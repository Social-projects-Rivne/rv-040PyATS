# Example
# -------
#
#   an example common setup

# import the aetest module

from pyats import aetest


# define a common setup section by inherting from aetest
class ScriptCommonSetup(aetest.CommonSetup):

    @aetest.subsection
    def check_script_arguments(self):
        pass

    @aetest.subsection
    def connect_to_devices(self):
        pass

    @aetest.subsection
    def configure_interfaces(self):
        pass
