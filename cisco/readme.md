big_config - large config file for cisco ASA
c3745 - config file for cisco 3745
c3725 - config file for cisco 3725
running-config - default config file for cisco ASA

configs.yaml, mapping.yaml, subsection.yaml, trigger.yaml, verification.yaml, testbed.yaml - files with configurations for genie run

test_pyats.py, test_asa - scripts for testing devices within pyats

-run tests within easypy and genie run: 'easypy <job file>.py -testbed_file <path to testbed file>'
-run tests within pyats: 'python <test_file>.py -testbed_file <path to testbed file>' 