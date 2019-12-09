# -*- coding:utf-8 -*-
import sys
sys.path.insert(0, '../../..')
import os

from lingua.algorithms.clustering.lda_model import LDAModelWrapper


REMOVE_WORDS = ['可口可乐', '卡特彼勒', '宝洁公司', '亨', '宝洁', '雪佛龙', 
                '护舒宝', '优尼科', '埃克森', '亚马逊', '霍尼韦尔', '戴尔',
                '大都会', '默沙东', '迪士尼', '浪', '波音', '强生', '思科',
                '斯', '贝', '伦', '谢', '人寿', '徐州', '无锡', '广西',
                '河南省', '河北省', '人寿']


def get_docs(path, suffix):
  def _func(w):
    if (w not in REMOVE_WORDS) and len(w) > 1 and \
       (not '小学' in w) and (not '县' in w) and \
       (not '可口可乐' in w) and (not '中学' in w):
        return True
    return False
  docs = []
  for f in os.listdir(path):
    if f.endswith(suffix):
      with open(os.path.join(path, f), 'r') as file:
        text = file.read()
    else:
      continue
    docs.append([x for x in text.lower().split() if _func(x)])
  return docs



if __name__ == '__main__':
  zh_docs = get_docs('/Users/junr/Documents/git/lingua/data/20191206-pdf/chinese', 'clean_fenci.txt')
  en_docs = get_docs('/Users/junr/Documents/git/lingua/data/20191206-pdf/english', 'clean_lemm.txt')

  zh_model = LDAModelWrapper(min_count=20,
                             no_below=1,
                             no_above=0.2,
                             num_topics=6,
                             chunksize=2000,
                             passes=20,
                             iterations=400,
                             eval_every=None,
                             verbose=True)
  # zh_model.preprocess(zh_docs)
  # zh_model.train()
  # zh_model.get_topics()



  en_model = LDAModelWrapper(min_count=20,
                             no_below=1,
                             no_above=0.2,
                             num_topics=6,
                             chunksize=2000,
                             passes=20,
                             iterations=400,
                             eval_every=None,
                             verbose=True)
  en_model.preprocess(en_docs)
  en_model.train()
  en_model.get_topics()


