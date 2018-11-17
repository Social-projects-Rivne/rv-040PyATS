from unicon import Connection
from pyats.topology import loader
from pyats.utils.fileutils import FileUtils

dev = Connection(hostname='DESKTOP-K0K4BRM',
                 start=['ssh vagrant@192.169.0.104'],
                 password='vagrant',
                 os='linux')

out = dev.execute("ifconfig")
tb = loader.load('testbed.yaml')

fils = FileUtils(testbed=tb)

fils.copyfile(
    source=r"scp:/vagrant@192.169.0.104/test/test",
    destination="/home/a/Desktop/"
)
