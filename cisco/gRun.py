import os

from ats.datastructures.logic import And, Not, Or
from genie.harness.main import gRun


def main():
    # Relative path of where the mapping datafile is
    test_path = os.path.dirname(os.path.abspath(__file__))

    # trigger_uids limit which test to execute
    # verification_uids limit which test to execute
    gRun(mapping_datafile=os.path.join(test_path, 'mapping.yaml'),
         # config_datafile=os.path.join(test_path, 'configs.yaml'),
         # verification_datafile=os.path.join(test_path, 'verification.yaml'),
         # pts_datafile=os.path.join(test_path, 'pts.yaml'),
         # pts_features=['interface'],
         # trigger_datafile=os.path.join(test_path, 'trigger.yaml'),
         verification_uids=Or('Verify_Interfaces'),
         subsection_datafile=os.path.join(test_path, 'subsection.yaml'),
         # filetransfer_protocol='tftp'
         )

# easypy <job file>.py -testbed_file <path to testbed file>
# easypy gRun.py -testbed_file testbed.yaml
