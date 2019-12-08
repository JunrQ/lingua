# -*- coding:utf-8 -*-

import os

class Stopwords(object):
  def __init__(self, id):
    """
    Parameters
    ----------
    id : int
      使用的停用词表的序号
    """
    self._id = id
    self._build()

  def _build(self):
    if self._id == 1:
      f = '百度停用词表.txt'
    elif self._id == 2:
      f = '哈工大停用词表.txt'
    elif self._id == 3:
      f = '四川大学机器智能实验室停用词库.txt'
    elif self._id == 4:
      f = '中文停用词表.txt'
    else:
      raise ValueError('Not support stopwords type: $d' % self._id)

    with open(os.path.join(os.path.dirname(__file__), f), 'r', encoding='utf-8') as file:
      words = file.readlines()
    self._words = [w.strip().lower() for w in words]

  @property
  def words(self):
    return self._words
