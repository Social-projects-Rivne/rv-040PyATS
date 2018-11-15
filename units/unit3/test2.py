from urllib.parse import urlparse
from units.unit3.test1 import FileUtils as FileUtilsXyzBase


class FileUtils(FileUtilsXyzBase):

    def copyfile(self, source, destination,
            timeout_seconds = 1200,
            *args, upload, **kwargs):

        from_parsed_url = urlparse(source)
        to_parsed_url = urlparse(destination)
        if upload:
            from_path = from_parsed_url.path

            to_server_name = to_parsed_url.hostname
            to_parsed_port = to_parsed_url.port
            to_path = to_parsed_url.path
            server_name = to_server_name
            port = to_parsed_port
        else:
            to_path = to_parsed_url.path
            from_server_name = from_parsed_url.hostname
            from_parsed_port = from_parsed_url.port
            from_path = from_parsed_url.path

            server_name = from_server_name
            port = from_parsed_port

        # Get auth details
        username, password = self.get_auth(server_name)

        # Transfer the file by executing commands on the device.
        if upload:
            upload_ftp_file(
                from_path=from_path,
                to_path=to_path,
                device=self.parent.device,
                username=username,
                password=password,
                timeout=timeout_seconds)
        else:
            download_ftp_file(
                from_path=from_path,
                to_path=to_path,
                device=self.parent.device,
                username=username,
                password=password,
                timeout=timeout_seconds)