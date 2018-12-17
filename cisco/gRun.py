import os

from ats.datastructures.logic import And, Not, Or
from genie.harness.main import gRun


def main():
    # Relative path of where the mapping datafile is
    test_path = os.path.dirname(os.path.abspath(__file__))

    # trigger_uids limit which test to execute
    # verification_uids limit which test to execute
    gRun(mapping_datafile=os.path.join(test_path, 'mapping.yaml'),
         config_datafile=os.path.join('configs.yaml'),
         filetransfer_protocol='scp'
         )

# easypy <job file>.py -testbed_file <path to testbed file>
