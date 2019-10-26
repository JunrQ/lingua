# -*- coding:utf-8 -*-

"""Some instances of TextDataset"""

from lingua.dataset.text_dataset import FilesTextDataset


def get_crawler_result_dataset(
  directory=['../data/crawler_result', '../data/ctrip_crawler_result']):
  file_text_ds = FilesTextDataset(directory, suffix='.txt',
                                  skip_head_line=1,
                                  skip_tail_line=1)
  def _line_process_func(l):
    l = l.strip()
    if len(l) < 5:
      return None
  file_text_ds.set_line_process_func(_line_process_func)
