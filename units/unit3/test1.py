from pyats.utils.fileutils import FileUtils as FileUtilsBase

class FileUtils(FileUtilsBase):
  DEFAULT_COPY_TIMEOUT_SECONDS = 1200

  def close(self):
      """ Deallocate any resources being held.  """
      for child_name, child_obj in self.children.items():
          child_obj.close()


  def copyfile(self, source, destination,
          timeout_seconds = DEFAULT_COPY_TIMEOUT_SECONDS,
          *args, **kwargs):
      """ Copy a file to/from a remote server. """

      from_scheme = self.get_scheme(source)
      to_scheme = self.get_scheme(destination)

      from_scheme_is_local = self.is_local(source)
      to_scheme_is_local = self.is_local(destination)

      if from_scheme_is_local and to_scheme_is_local:
          raise Exception("fileutils module {} does not allow "
              "copying between two local files.".format(self.__module__))

      if not from_scheme_is_local and not to_scheme_is_local:
          raise Exception("fileutils module {} does not allow "
              "copying between two remote files.".format(self.__module__))


      abstraction_scheme = to_scheme if from_scheme_is_local else from_scheme

      # Get implementation
      child = self.get_child(abstraction_scheme, **kwargs)

      # Execute copy
      return child.copyfile(source, destination, timeout_seconds,
          *args, upload=from_scheme_is_local, **kwargs)