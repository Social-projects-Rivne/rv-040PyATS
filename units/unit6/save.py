"""save.py for make direction reports"""

import logging
import shutil

from pyats.easypy.plugins.bases import BasePlugin

LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.INFO)


class CopyReport(BasePlugin):
    """Main class for reporting"""

    def __init__(self, directory, *args, **kwargs):
        """Initialize directories from yaml file. Args from plugins configuration file"""
        super().__init__(*args, **kwargs)
        self._source = directory

    def post_job(self, job):
        """Copy custom test files to archive and print some info"""
        directory = job.runtime.testbed.custom.get('directory')
        report_directory = job.runtime.testbed.custom.get('report_directory')
        LOGGER.info('The directory to copy: %s;	destination: %s', directory, report_directory)
        shutil.copytree(directory, '{}/{}'.format(job.runtime.directory, report_directory))
