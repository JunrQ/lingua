# -*- coding:utf-8 -*-

import os
import pdfminer

from lingua.dataset.dataset import BaseDataset


class PdfDataset(BaseDataset):
  """Pdf dataset."""
  def __init__(self, pdf_files):
    if not isinstance(pdf_files, list):
      pdf_files = [pdf_files]
    self._files = pdf_files

  # def 

  def pdf2text(self, input_pdf):
    file_name = os.path.basename(input_pdf)
    file_name, _ = os.path.splitext(file_name)
    print(file_name)
    tmp_outpu_file_name = 'pdf2text_%s_tmpe.txt' % file_name

    # Call pdfminer command line
    command_line = "python {2} -o {0} " \
                   "-t text {1}".format(tmp_outpu_file_name,
                                        input_pdf,
                                        os.path.join('pdfminer', 'tools', 'pdf2txt.py'))
    os.system(command_line)
    with open(tmp_outpu_file_name, 'w') as f:
      text = f.readlines()
    os.remove(tmp_outpu_file_name)
    return text

  def parse_pdfs(self, output_type='text'):
    assert output_type in ['text', 'html']
    text_list = []
    for f in self._files:
      try:
        if output_type == 'text':
          output = self.pdf2text(f)
        elif output_type == 'html':
          output = self.pdf2html(f)
      except Exception as e:
        print(e)
        continue
      text_list.append(output)
      








