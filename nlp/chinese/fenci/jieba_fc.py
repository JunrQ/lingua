# -*- coding:utf-8 -*-

# Provide wrapper for jieba 分词

import jieba

from lingua.nlp.chinese.fenci import BaseFenci

class JiebaFenci(BaseFenci):
  def __init__(self, cut_all=False,
               HMM=False,
               stopwords_id=1):
    """
    Parameters
    ----------
    cut_all : bool
      控制是否采用全模式
    HMM : bool
      控制是否使用HMM模型
    """
    jieba.initialize()
    self._cut_all = cut_all
    self._hmm = HMM
    super(JiebaFenci, self).__init__(stopwords_id=stopwords_id)

  def load_dict(self, dict):
    raise NotImplementedError()

  def add_word(self, word, freq=None, tag=None):
    jieba.add_word(word, freq=freq, tag=tag)

  def __call__(self, text):
    words = jieba.cut(text, cut_all=self._cut_all, HMM=self._hmm)
    words = [w.strip() for w in words]
    words = [w for w in words if len(w) > 0]
    words = self._rm_stopwords(words)
    return words
