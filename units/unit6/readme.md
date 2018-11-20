#if error with yaml file
export PYTHONPATH=${PWD}/plugins:${PYTHONPATH}

#run
easypy -configuration <path>/plugin_homework.yaml <path>/job_homework.py

#run by testbed
easypy <path>/job_homework.py -testbed_file <path>/testbase.yaml