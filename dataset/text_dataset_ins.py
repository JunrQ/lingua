# -*- coding:utf-8 -*-

"""Some instances of TextDataset"""

import os
from functools import partial

from lingua.dataset.text_dataset import FilesTextDataset
from lingua.dataset.utils_string import encode_decode_rm_specified_code, \
   connect_some_f_pattern

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
  return file_text_ds


def get_pdf2html2txt_result_dataset():
  root_path = '/Users/junr/Documents/git/lingua/data/pdf/'
  direcotries = [os.path.join(root_path, x) for x in os.listdir(root_path)]
  pdf_txt_ds = FilesTextDataset(direcotries, suffix='.txt',
                                skip_head_line=1, skip_tail_line=1)
  pdf_txt_ds.add_line_process_func(encode_decode_rm_specified_code)
  pdf_txt_ds.add_line_process_func(partial(connect_some_f_pattern, infix='fi'))
  pdf_txt_ds.add_line_process_func(partial(connect_some_f_pattern, infix='ff'))
  return pdf_txt_ds
