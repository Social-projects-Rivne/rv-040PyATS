"""File for terminal running by easypy"""

import os

from pyats.easypy.tasks import run

PROJECT_DIR = os.path.dirname(__file__)


def main():
    """Main method for running by easypy"""
    run(testscript=os.path.join(PROJECT_DIR, 'tb.py'))
