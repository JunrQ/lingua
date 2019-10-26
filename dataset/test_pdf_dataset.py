# -*- coding:utf-8 -*-

import sys
sys.path.insert(0, '../..')

import os

from lingua.dataset.pdf_dataset import PdfDataset
from lingua.dataset.utils_path import list_files

if __name__ == '__main__':
  pdf_directory = os.path.join('..', 'data', 'pdf')
  pdf_dir_list = []
  for d in os.listdir(pdf_directory):
    pdf_directories = os.path.join(pdf_directory, d)
    if os.path.isdir(pdf_directories):
       pdf_dir_list.append(pdf_directories)
  pdf_files_list = []
  for d in pdf_dir_list:
    cur_dir_pdf_files = list_files(d, suffix='pdf')
    pdf_files_list += cur_dir_pdf_files

  pdf_dataset_instance = PdfDataset(pdf_files_list)

  # import pdb; pdb.set_trace()
  text = pdf_dataset_instance.pdf2text(pdf_files_list[0])

  print(pdf_files_list[0])
  print(text)

