export PYTHONPATH=${PWD}

easypy job.py -testbed_file testbed.yaml -configuration plugins.yaml -archive_dir data

cd archive

unzip ...