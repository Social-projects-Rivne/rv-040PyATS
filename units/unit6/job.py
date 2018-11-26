"""job.py for easypy run"""

import os
from pyats import easypy

PROJECT_DIR = os.path.dirname(__file__)


def main():
    """Main function for easypy run"""
    easypy.run(testscript='test.py')
