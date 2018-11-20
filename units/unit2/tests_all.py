"""For running tasks in 4 threads"""

import argparse
import os
import sys
import time
from datetime import timedelta

from pyats.easypy import Task


def main(runtime):

    parser = argparse.ArgumentParser(description="Standalone parser")
    parser.add_argument('-num1', type=float, required=True)
    parser.add_argument('-num2', type=float, required=True)
    args, sys.argv[1:] = parser.parse_known_args(sys.argv[1:])

    # using Task class to create a 4 tasks
    # (max runtime = 60*5 seconds = 1 minutes)
    task_multiplication = Task(testscript=os.path.dirname(__file__) + '/multiplication.py',
                               runtime=runtime,
                               taskid='multiplication',
                               num1=args.num1,
                               num2=args.num2)
    task_division = Task(testscript=os.path.dirname(__file__) + '/division.py',
                         runtime=runtime,
                         taskid='division',
                         num1=args.num1,
                         num2=args.num2)
    task_addition = Task(testscript=os.path.dirname(__file__) + '/addition.py',
                         runtime=runtime,
                         taskid='addition',
                         num1=args.num1,
                         num2=args.num2)
    task_subtraction = Task(testscript=os.path.dirname(__file__) + '/subtraction.py',
                            runtime=runtime,
                            taskid='subtraction',
                            num1=args.num1,
                            num2=args.num2)
    # start both tasks simultaneously
    task_multiplication.start()
    task_division.start()
    task_addition.start()
    task_subtraction.start()
    # poll for tasks to finish (max of 1 minutes)
    counter = timedelta(minutes=1)
    while counter:
        # check if processes are alive, if so, continue to wait
        if task_multiplication.is_alive() \
                or task_division.is_alive() \
                or task_addition.is_alive() \
                or task_subtraction.is_alive():
            time.sleep(1)
            counter -= timedelta(seconds=1)
        else:
            # all is good
            break
    else:
        # exceeded runtime
        task_multiplication.terminate()
        task_multiplication.join()
        task_division.terminate()
        task_division.join()
        task_addition.terminate()
        task_addition.join()
        task_subtraction.terminate()
        task_subtraction.join()
        # raise exception
        raise TimeoutError('Not all tasks finished in 5 minutes!')
