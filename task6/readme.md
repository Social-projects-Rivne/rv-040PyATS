export PYTHONPATH=${PWD}

easypy job.py -testbed_file testbed.yaml -configuration plugins.yaml

cd archive

unzip ...