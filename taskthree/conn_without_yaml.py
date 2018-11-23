from unicon import Connection
from pyats.topology import loader
from pyats.utils.fileutils import FileUtils

dev = Connection(hostname='DESKTOP-K0K4BRM',
                 start=['ssh vagrant@192.169.0.0'],
                 password='vagrant',
                 os='linux')

