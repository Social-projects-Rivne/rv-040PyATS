export PYTHONPATH=${PWD}/plugins:${PYTHONPATH}

easypy job.py

??????
easypy -configuration plugins.yaml job.py

?????
easypy job_homework.py -testbed_file testbase.yaml