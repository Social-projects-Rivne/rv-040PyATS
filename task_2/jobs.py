"""
easypy task_2/jobs.py -num1 <num1> -num2 <num2>

"""
import argparse
import time
from datetime import timedelta
import sys
import os

from pyats.easypy.tasks import Task

dir_name = os.path.dirname(__file__)

parser = argparse.ArgumentParser(description="Math function tests")
parser.add_argument('-num1', type=float, required=True)
parser.add_argument('-num2', type=float, required=True)


def main(runtime):

    args, sys.argv[1:] = parser.parse_known_args(sys.argv[1:])

    # using Task class to create a two tasks
    # max runtime = 60*5 sec = 5 min
    task_add = Task(testscript=(os.path.join(dir_name + '/jobs/addition.py')),
                    runtime=runtime,
                    taskid='Add test',
                    num1=args.num1,
                    num2=args.num2)

    task_sub = Task(testscript=(os.path.join(dir_name + '/jobs/substraction.py')),
                    runtime=runtime,
                    taskid='Sub test',
                    num1=args.num1,
                    num2=args.num2)

    task_mult = Task(testscript=(os.path.join(dir_name + '/jobs/multiplication.py')),
                    runtime=runtime,
                    taskid='Mult test',
                    num1=args.num1,
                    num2=args.num2)

    task_div = Task(testscript=(os.path.join(dir_name + '/jobs/division.py')),
                    runtime=runtime,
                    taskid='Div test',
                    num1=args.num1,
                    num2=args.num2)



    all_tasks = [task_add, task_sub, task_mult, task_div]

    #start all tasks simultaneously
    for task in all_tasks:
        task.start()

    # poll for tasks to finish (max of 5 minutes)
    counter = timedelta(minutes=5)

    while counter:

        # check if processes are alive, if so, continue to wait
        if any(task.is_alive() for task in all_tasks):
            time.sleep(1)
            counter -= timedelta(seconds=1)
        else:
            break

    else:
        for task in all_tasks:
            task.terminate()
            task.join()

        #raise exception
        raise TimeoutError('Not all tasks finished in 5 minutes')




