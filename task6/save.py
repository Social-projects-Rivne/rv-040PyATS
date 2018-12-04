import logging
import shutil

from pyats.easypy.plugins.bases import BasePlugin

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class CopyReport(BasePlugin):
    def __init__(self, directory, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._source = directory

    def post_job(self, job):
        self.dest = job.runtime.testbed.custom.get('report_directory')
        logger.info('The directory to copy: %s; destination: %s', self._source, self.dest)
        shutil.copytree(self._source, '{}/{}'.format(job.runtime.directory, self.dest))


