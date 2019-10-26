# -*- coding:utf-8 -*-

# Some util functions for processing paths.

import os

def list_files(directory, prefix='', suffix=''):
  """List all files under directory with specified prefix and suffix.

  Parameters
  ----------
  directory : str
    Directory to traverse.
  prefix : str, optional
    Prefix of files.
  suffix : str, optional
    Suffix of files.
  
  Returns
  ------
  files_list : `list` of files
  """
  if not os.path.isdir(directory):
    raise ValueError("%s is not a directory")
  files_list = []
  for f in os.listdir(directory):
    if len(prefix):
      if not f.startswith(prefix):
        continue
    if len(suffix):
      if not f.endswith(suffix):
        continue
    files_list.append(os.path.join(directory, f))
  return files_list
