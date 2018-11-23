"""easypy runer"""

import argparse
import sys
import os


from pyats.easypy.tasks import run


def main():
    parser = argparse.ArgumentParser(description="standalone parser")
    parser.add_argument('-word', type=str, default='alongggggggggggggword', required=False)
    args, sys.argv[1:] = parser.parse_known_args(sys.argv[1:])
    run(testscript=os.path.dirname(__file__) + '/rabbit.py', word=args.word)