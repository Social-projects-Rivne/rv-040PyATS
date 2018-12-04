"""easypy job to copy files"""

import os.path

from pyats.easypy.tasks import run


dir_name = os.path.dirname(__file__)


def main():
    run(testscript=dir_name + "/conn_test.py")
