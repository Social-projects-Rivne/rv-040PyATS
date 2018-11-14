"""Common setup"""


from pyats import aetest


class ScriptCommonSetup(aetest.CommonSetup):
    # define a common setup section by inherting from aetest

    @aetest.subsection
    def check_script_arguments(self):
        pass

    @aetest.subsection
    def connect_to_devices(self):
        pass

    @aetest.subsection
    def configure_interfaces(self):
        pass
