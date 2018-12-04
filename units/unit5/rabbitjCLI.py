"""Testbed file for terminal running"""

import argparse
import os
import sys

from pyats.easypy.tasks import run

PROJECT_DIR = os.path.dirname(__file__)


def main():
    """Main function for running by easypy"""
    # parser arguments for command line
    parser = argparse.ArgumentParser(description="Standalone parser")
    parser.add_argument('-word', type=str, default='alongggggggggggggword', required=False)
    args, sys.argv[1:] = parser.parse_known_args(sys.argv[1:])
    # run
    run(testscript=os.path.join(PROJECT_DIR, 'rabbitCLI.py'), word=args.word)
