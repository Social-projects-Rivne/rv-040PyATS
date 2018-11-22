"""
easypy tasktwo/jobs.py -num1 <num1> -num2 <num2>

"""
import argparse
import time
from datetime import timedelta
import sys
import os

from pyats.easypy.tasks import Task

dir_name = os.path.dirname(__file__)

parser = argparse.ArgumentParser(description="my custom parser")
parser.add_argument('-num1', type = int, required=True)
parser.add_argument('-num2', type = int, required=True)

def main(runtime):

    args, sys.argv[1:] = parser.parse_known_args(sys.argv[1:])

    #using Task class to create a two tasks
    # max runtime = 60*5 sec = 5 min
    task_add = Task(testscript = (os.path.join(dir_name + '/jobs/addition.py')),
                    runtime=runtime,
                    taskid='add',
                    num1=args.num1,
                    num2=args.num2)

    task_sub = Task(testscript = (os.path.join(dir_name + '/jobs/substraction.py')),
                    runtime=runtime,
                    taskid='sub',
                    num1=args.num1,
                    num2=args.num2)

    task_mult = Task(testscript = (os.path.join(dir_name + '/jobs/multiplication.py')),
                    runtime=runtime,
                    taskid='mult',
                    num1=args.num1,
                    num2=args.num2)

    task_div = Task(testscript =(os.path.join(dir_name + '/jobs/division.py')),
                    runtime=runtime,
                    taskid='div',
                    num1=args.num1,
                    num2=args.num2)


    #start both tasks simultaneously
    task_add.start()
    task_sub.start()
    task_mult.start()
    task_div.start()

    # poll for tasks to finish (max of 5 minutes)
    counter = timedelta(minutes=5)

    while counter:
        # check if processes are alive, if so, continue to wait
        if task_add.is_alive() or task_sub.is_alive() \
            or task_div.is_alive() or task_mult.is_alive():
            time.sleep(1)
            counter -= timedelta(seconds=1)

        else:
            #all is good
            break

    else:
        # exceeded runtime
        task_add.terminate()
        task_add.join()
        task_sub.terminate()
        task_sub.join()
        task_mult.terminate()
        task_mult.join()
        task_div.terminate()
        task_div.join()

        #raise exception
        raise TimeoutError('Not all tasks finished in 5 minutes')




