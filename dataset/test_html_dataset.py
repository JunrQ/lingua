import sys
sys.path.insert(0, '../..')
import os

from html_dataset import HTMLDataset
from utils_path import list_files
from text_dataset_ins import get_pdf2html2txt_result_dataset
from utils_string import encode_decode_rm_specified_code

if __name__ == "__main__":
  # - Test one
  # html = '/Users/junr/Documents/git/lingua/data/pdf/3M/2017-sustainability-report.pdf.html'
  # html_ds = HTMLDataset(html)
  # html_ds.get_text()

  # - Test two
  # p = '/Users/junr/Documents/git/lingua/data/pdf/'
  # for d in os.listdir(p):
  #   dp = os.path.join(p, d)

  #   for f in list_files(dp, suffix='.pdf'):
  #     print(f)
  #     htmlf = f + '.html'
  #     if not os.path.isfile(htmlf):
  #       continue
  #       print("%s not exist, transfer..." % htmlf)
  #       term_com = 'pdf2htmlEX --zoom 1.3 "%s" "%s"' % (f, htmlf)
  #       os.system(term_com)
  #       if not os.path.isfile(htmlf):
  #         print("[WARNING] Fail to convert %s to html" % f)
  #         continue
  #     txtf = f + '.txt'
  #     # if os.path.isfile(txtf):
  #     #   print("%s already exist, skip..." % txtf)
  #     html_ds = HTMLDataset(htmlf)
  #     html_ds.save_to(txtf)


  # - Test 3
  pdf_txt_ds = get_pdf2html2txt_result_dataset()
  for l in pdf_txt_ds.get_lines():
    print(l)
    

