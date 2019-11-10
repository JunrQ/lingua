from functools import reduce

from lingua.nlp.preprocess import utils
from lingua.nlp.mining.rake import Rake


# class RAKE(object):
#   """Paper: Automatic keyword extraction from individual documents."""
#   def __init_(self):
#     self._sentence_token = utils.sentence_tokenize()
#     self._word_token = utils.word_tokenize()
#     self._stop_words_rm = utils.remove_stop_words()
#     self._replace_abbr_not = utils.replace_abbr_not()
#     self._replace_repeat_letters = utils.replace_repeat_letters()
#     self._word_lemm = utils.word_lemmatizing()

#   def _word_score(self, word_list):
#     word_frequence = {}
#     word_degree = {}

#   def __call__(self, text):
#     text = self._replace_abbr_not(text)
#     sentence_list = self._sentence_token(text)
#     candidate_keywords = reduce(lambda x, y : x + y, 
#       [self._word_token(z) for z in sentence_list])
#     candidate_keywords = self._word_lemm(
#       self._replace_repeat_letters( # For review
#       self._stop_words_rm(candidate_keywords)))
    
class RAKE(object):
  """A wrapper of Rake from *git@github.com:csurfer/rake-nltk.git*"""
  def __init__(self, stopwords=None,
               punctuations=None,
               language="english",
               max_length=100000,
               min_length=1):
    self._raker = Rake(stopwords=stopwords, punctuations=punctuations,
                       language=language, max_length=max_length,
                       min_length=min_length)

  def __call__(self, text, scores=False):
    if isinstance(text, str):
      self._raker.extract_keywords_from_text(text)
    elif isinstance(text, list):
      self._raker.extract_keywords_from_sentences(text)
    else:
      raise TypeError("Except str of list of str, but got %s" % type(text))
    if scores:
      return self._raker.get_ranked_phrases_with_scores()
    else:
      return self._raker.get_ranked_phrases()

