"""job.py"""

import argparse
import sys
import time

from datetime import timedelta
from pyats.easypy import Task


parser = argparse.ArgumentParser(description="standalone parser")
parser.add_argument('-num1',  type=float, required=True)
parser.add_argument('-num2',  type=float, required=True)
args, sys.argv[1:] = parser.parse_known_args(sys.argv[1:])


def main(runtime):
    division = Task(testscript='division.py',
                    runtime = runtime,
                    taskid = "division",
                    num1 = args.num1,
                    num2 = args.num2)

    addition = Task(testscript='addition.py',
                    runtime = runtime,
                    taskid = "addition",
                    num1 = args.num1,
                    num2 = args.num2)

    subtraction = Task(testscript='subtraction.py',
                       runtime = runtime,
                       taskid = "subtraction",
                       num1 = args.num1,
                       num2 = args.num2)

    multiplication = Task(testscript='multiplication.py',
                          runtime = runtime,
                          taskid = "multiplication",
                          num1 = args.num1,
                          num2 = args.num2)

    division.start()
    addition.start()
    subtraction.start()
    multiplication.start()

    counter = timedelta(minutes = 1)

    while counter:
        # chek if processes are alive, if so, continue wait
        if division.is_alive() or addition.is_alive() or subtraction.is_alive() or multiplication.is_alive():
            time.sleep(1)
            counter -= timedelta(seconds = 1)
        else:
            break
    else:
        division.terminate()
        division.join()

        addition.terminate()
        addition.join()

        subtraction.terminate()
        subtraction.join()

        multiplication.terminate()
        multiplication.join()

        raise TimeoutError("1 minute have passed")