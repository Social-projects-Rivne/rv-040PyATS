"""save_homework.py for make direction reports"""

import logging
import shutil

from pyats.easypy.plugins.bases import BasePlugin

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class CopyReport(BasePlugin):
    """Main class for reporting"""

    def __init__(self, directory, *args, **kwargs):
        """Initialize directories from yaml file"""
        super().__init__(*args, **kwargs)
        self._source = directory

    def post_job(self, job):
        """Copy runinfo to report directory and print some info"""
        report_directory = job.runtime.testbed.custom.get('report_directory')
        logger.info('The directory copy to destination: %s', report_directory)
        # shutil.move(job.runtime.directory, report_directory)
        # shutil.make_archive()
        # shutil.copy(job.runtime.archive, report_directory, follow_symlinks=False)
