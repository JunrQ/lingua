# -*- coding:utf-8 -*-

from lingua.dataset.dataset import BaseDataset
from lingua.dataset.utils_path import list_files


class TextDataset(BaseDataset):
  """TextDataset Base Class"""

  def get_lines(self):
    """An iterator which yield lines."""
    raise NotImplementedError()

  def set_line_process_func(self, func):
    """Set function to process a line."""
    self._line_func = func
  
  def add_line_process_func(self, func):
    """Add line processes function in a pipeline."""
    self._added_line_func.append(func)


class FilesTextDataset(TextDataset):
  """Get all text from files under some directory"""
  def __init__(self, paths,
               prefix='', suffix='',
               line_process_func=None,
               skip_head_line=False,
               skip_tail_line=False):
    """ 
    Parameters
    ----------
    paths : str or list of str
      Paths that take considerate of.
    prefix : str
      Prefix of files.
    suffix : str
      Suffix of files.
    line_process_func : function
      Used to process every lines.
    skip_head_line : bool or int
      True means skip first line, an int means skip
      first skip_head_line lines.
    skip_tail_line : bool or int
      True means skip last line, an int means skip
      last skip_tail_line lines.
    """
    self._paths = paths
    self._prefix = prefix
    self._suffix = suffix
    self._file_list = list_files(self._paths, self._prefix, self._suffix)
    self._line_func = line_process_func
    self._added_line_func = []
    def _int_if_bool(v):
      if isinstance(v, bool):
        v = 1 if v else 0
      elif isinstance(v, int):
        pass
      else:
        raise ValueError("Expect bool or int, but got %s" % type(v))
      return v
    self._skip_head_line = _int_if_bool(skip_head_line)
    self._skip_tail_line = _int_if_bool(skip_tail_line)

  @property
  def files(self):
    return self._file_list

  def single_file_get_lines(self, fp):
    line_pool = []
    with open(fp, 'r') as f:
      for i, l in enumerate(f.readlines()):
        if i < self._skip_head_line:
          continue
        if len(line_pool) < self._skip_tail_line:
          line_pool.append(l)
          continue
        line_pool.append(l)
        l = line_pool.pop(0)
        if self._line_func is not None:
          l = self._line_func(l)
        if len(self._added_line_func) > 0:
          for tmp_f in self._added_line_func:
            l = tmp_f(l)
        if l:
          yield l
        else:
          continue

  def get_lines(self):
    for fp in self._file_list:
      self.single_file_get_lines(fp)
