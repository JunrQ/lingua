
import os
from wordcloud import WordCloud as WC
import cv2
from collections import Counter

from lingua.nlp.preprocess.utils import remove_pattern, \
    remove_single_letter_words, replace_abbr_not, \
    replace_repeat_letters, correct_spelling, \
    sentence_tokenize, remove_len_less_than, \
    word_tokenize, remove_stop_words, \
    word_lemmatizing


class WordCloud(object):
  def __init__(self):
    self._min_word_len = 1
    self._text_processors = [
      replace_abbr_not(),
      # remove_len_less_than(3),
      sentence_tokenize(),
    ]
    self._sentence_processors = [
      word_tokenize(),
      remove_stop_words(),
    ]
    self._words_processors = [
      word_lemmatizing(),
      correct_spelling(),
    ]
    self._word_list = []

    self._wc = WC(max_words=100, font_path=None,
                  background_color='white',
                  # width=400, height=200,
                  mask=cv2.imread('word_cloud.mask0.png'))

  def add_text(self, text):
    for func in self._text_processors:
      text = func(text)
    words = []
    for senc in text:
      for func in self._sentence_processors:
        senc = func(senc)
      words += senc
    res = []
    for w in words:
      if len(w) > self._min_word_len:
        for func in self._words_processors:
          w = func(w)
          if len(w) > self._min_word_len:
            res.append(w.lower())
    self._word_list += res

  def add_file(self, filename):
    with open(filename, 'r') as f:
      text = f.read()
    self.add_text(text)

  def generate_word_cloud(self, filename, reset=True):
    word_counter = Counter(self._word_list)
    # self._wc.generate_from_text(' '.join(self._word_list))
    self._wc.generate_from_frequencies(dict(word_counter))
    self._wc.to_file(filename)
    if reset:
      self.reset()

  def reset(self):
    self._word_list = []
