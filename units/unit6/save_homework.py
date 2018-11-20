# plugins/save.py

import logging
import shutil

from pyats.easypy.plugins.bases import BasePlugin
from pyats.topology import Testbed

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


# class CopyReport(BasePlugin):
#
#     def __init__(self, directory, report_directory, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self._directory = directory
#         self._report_directory = report_directory
#
#     def post_job(self, job):
#         logger.info('The directory to copy: %s;	destination: %s', self._directory, self._report_directory)
#         print(job.runtime.archive)
#         print(job.runtime.testbed)
#         shutil.copytree(job.runtime.directory, self._report_directory)


class CopyReport(Testbed):
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    # def post_job(self, job):
    #     # logger.info('The directory to copy: %s;	destination: %s', self._directory, self._report_directory)
    #     print(job.runtime.archive)
    #     print(job.runtime.testbed)
    #     # shutil.copytree(job.runtime.directory, self._report_directory)
