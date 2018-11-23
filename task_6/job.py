"""job.py for easypy run"""

from pyats import easypy


def main():
    """Main function for easypy run"""
    easypy.run(testscript='test.py')
