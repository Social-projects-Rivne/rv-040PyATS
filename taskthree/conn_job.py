"""easypy job to copy files"""

import os.path

dir_name = os.path.dirname(__file__)
from pyats.easypy.tasks import run


def main():
    run(testscript=dir_name + "/conn_test.py")
