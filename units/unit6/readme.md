Your task is to integrate this testbed file with the code from "plugins for easypy " section. The directory option from testbed file has
to be used within the tests to determine a directory, which is used for storing tests files. The CopyReport plugin has to use
directory option as a source directory. The report-directory option has to be used as a destination directory within a report
archive.

#if error with yaml file
export PYTHONPATH=${PWD}

#run
easypy <path>/job.py -testbed_file <path>/testbase.yaml -configuration <path>/plugin.yaml