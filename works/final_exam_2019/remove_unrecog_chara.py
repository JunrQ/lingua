# -*- coding:utf-8 -*-

import re
import os

# make Chinese text clean
def clean_zh_text(text, replace=' ', remove_punc=False):
  # keep English, digital and Chinese
  # r1 = u'[a-zA-Z0-9’!"#$%&\'()*+,-./:;<=>?@，。?★、…【】《》？“”‘’！[\\]^_`{|}~]+'
  if not remove_punc:
    comp = re.compile('[^A-Z^a-z^\u4e00-\u9fa5\s’!"#$%&\'()*+,-./:;<=>?@，。?★、…【】《》？“”‘’！[\\]^_`{|}~]')
  else:
    comp = re.compile('[^\u4e00-\u9fa5\s]')
  return comp.sub(replace, text)


def work(path):
  print(path)
  fname, extname = os.path.splitext(path)
  output_name = fname + '_clean' + extname
  with open(path, 'r', encoding='utf-8') as f:
    text = f.read()
  text = clean_zh_text(text)
  with open(output_name, 'w', encoding='utf-8') as f:
    f.write(text)

def work1(path):
  print(path)
  fname, extname = os.path.splitext(path)
  output_name = fname + '_clean' + extname
  with open(path, 'r', encoding='utf-8') as f:
    text = f.read()
  text = clean_zh_text(text, replace='', remove_punc=True)
  with open(output_name, 'w', encoding='utf-8') as f:
    f.write(text)


def list_files(p, suffix='txt'):
  return [os.path.join(p, t) for t in os.listdir(p) if t.endswith(suffix)]

if __name__ == '__main__':
  cn_path = '/Users/junr/Documents/git/lingua/data/20191206-pdf/chinese'
  for p in list_files(cn_path):
    if 'clean' not in p:
      work1(p)
  
  en_path = '/Users/junr/Documents/git/lingua/data/20191206-pdf/english'
  for p in list_files(en_path):
    if 'clean' not in p:
      work(p)
