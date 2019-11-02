"""Define some normal processor instances."""

from functools import partial

from lingua.nlp.preprocess.utils import *
from lingua.nlp.preprocess.preprocessor import Processor


class WordLevelProcessor(Processor):
  """For word level analysis, like frequence.

  1. replace_abbr_not
  2. sentence_tokenize
  3. word_tokenize
  4. remove_stop_words
  5. correct_spelling
  6. word_lemmatizing
  """
  def __init__(self):
    super(WordLevelProcessor, self).__init__()
    self.add_func([
        # text level
        replace_abbr_not(),
        sentence_tokenize()
      ] +
      list(map(lambda x : partial(list_process_wrapper, x), [
        # sentence level
        word_tokenize(),
        remove_stop_words()
      ])) + 
      [partial(remove_len_less_than, minimum_length=2)] +
      list(map(lambda x : partial(list_list_process_wrapper, x), [
        # word level
        correct_spelling(),
        word_lemmatizing(),
      ]))
    )


class SentenceProcessor(Processor):
  """Common process to get senteces."""
  def __init__(self):
    super(SentenceProcessor, self).__init__()
    self.add_func([
      replace_abbr_not(),
      sentence_tokenize()
    ])

