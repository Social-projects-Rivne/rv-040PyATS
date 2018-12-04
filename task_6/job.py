"""job.py for easypy run"""
import os
from pyats import easypy

dir_name = os.path.dirname(__file__)

def main():
    """Main function for easypy run"""
    easypy.run(testscript=os.path.join(dir_name, 'test.py'))
