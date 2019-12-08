from lingua.nlp.chinese.stopwords import Stopwords

class BaseFenci(object):
  """Base class for fenci."""

  def __init__(self, stopwords_id):
    self._stopwords_id = stopwords_id
    if stopwords_id == 0:
      self._stopwords = []
    else:
      self._stopwords = Stopwords(stopwords_id).words

  def _rm_stopwords(self, words):
    res = [w for w in words if w not in self._stopwords]
    return res
