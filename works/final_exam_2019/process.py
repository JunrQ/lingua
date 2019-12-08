# -*- coding:utf-8 -*-
import sys
sys.path.insert(0, '../../..')
import os

from lingua.nlp.chinese.fenci.jieba_fc import JiebaFenci
from lingua.nlp.preprocess.utils import remove_pattern, \
    remove_single_letter_words, replace_abbr_not, \
    replace_repeat_letters, correct_spelling
from lingua.nlp.preprocess.processor_ins import WordLevelProcessor

fencior = JiebaFenci(stopwords_id=1)

def work_cn(path):
  print(path)
  fname, extname = os.path.splitext(path)
  output_name = fname + '_fenci' + extname
  with open(path, 'r', encoding='utf-8') as f:
    text = f.read()
  text = fencior(text)
  with open(output_name, 'w', encoding='utf-8') as f:
    f.write(' '.join(text))


text_level = [remove_single_letter_words(), replace_abbr_not(),
              word_tokenize()]
word_level = [remove_stop_words(), word_lemmatizing()]
def work_en(path):
  print(path)
  fname, extname = os.path.splitext(path)
  output_name = fname + '_fenci' + extname
  with open(path, 'r', encoding='utf-8') as f:
    text = f.read()
  for f in text_level:
    text = f(text)
  for f in word_level:
    text = f(text)
  text = fencior(text)
  with open(output_name, 'w', encoding='utf-8') as f:
    f.write(' '.join(text))



def list_files(p, suffix='clean.txt'):
  return [os.path.join(p, t) for t in os.listdir(p) if t.endswith(suffix)]


if __name__ == '__main__':
  cn_path = '/Users/junr/Documents/git/lingua/data/20191206-pdf/chinese'
  for p in list_files(cn_path):
    work_cn(p)
  
  # en_path = '/Users/junr/Documents/git/lingua/data/20191206-pdf/english'
  # for p in list_files(en_path):
  #   if 'clean' not in p:
  #     work(p)



