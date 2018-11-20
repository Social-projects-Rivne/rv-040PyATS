"""Testbed file for terminal running"""

import os

from pyats.easypy.tasks import run


def main():
    """Main method for running by easypy"""
    run(testscript=os.path.dirname(__file__) + '/tb.py')
