import re
import nltk
from nltk.tokenize import sent_tokenize as nltk_sent_tokenize, \
    word_tokenize as nltk_word_tokenize, WordPunctTokenizer as nltk_WP_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, LancasterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
from nltk.metrics import edit_distance
import enchant


def _class_decorator(name, use_func_name=False):
  # Make a function a class
  # TODO(zcq) May loss doc.
  def _func_decorator(func):
    def _wrapper(self, *args, **kwrags):
      return func(*args, **kwrags)
    name_str = name
    if use_func_name and hasattr(func, 'name'):
      name_str = func.name
    C = type(name, (object, ),
            {'__call__' : _wrapper,
             'name' : name_str})
    return C
  return _func_decorator


def remove_single_letter_words(text):
  return re.sub(r'(?<![\w\-])\w(?![\w\-])', '', text)


def list_process_wrapper(func, list_input):
  return [func(x) for x in list_input]


def list_list_process_wrapper(func, list_list_input):
  return [[func(w) for w in l] for l in list_list_input]


def remove_len_less_than(input, minimum_length=1):
  """Remove elements with lenght less than minimum_length."""
  if isinstance(input, str):
    raise ValueError("Except list of str, but got single string %s" 
                      % input)
  if isinstance(input[0], str):
    res = []
    for i in input:
      if len(i) >= minimum_length:
        res.append(i)
    return res
  res = []
  for i in input:
    inner_output = remove_len_less_than(i, minimum_length)
    if len(inner_output) > 0:
      res.append(inner_output)
  return res


# ---------------------- Text functions -----------------------
@_class_decorator('sentence_tokenize')
def sentence_tokenize(text):
  """Tokenize text into sentences."""
  return nltk_sent_tokenize(text)


@_class_decorator('remove_pattern')
def remove_pattern(text, pattern):
  text = re.sub(pattern, '', text)
  return text


class replace_abbr_not(object):
  """Replace '

  e.g.
  can't -> cannot
  i'm -> i am
  """
  def __init__(self):
    self.name = 'replace_abbr_not'
    replacement_patterns = [
      (r'won\'t', 'will not'),
      (r'can\'t', 'cannot'),
      (r'i\'m', 'i am'),
      (r'ain\'t', 'is not'),
      (r'(\w+)\'ll', '\g<1> will'),
      (r'(\w+)n\'t', '\g<1> not'),
      (r'(\w+)\'ve', '\g<1> have'),
      (r'(\w+)\'s', '\g<1> is'),
      (r'(\w+)\'re', '\g<1> are'),
      (r'(\w+)\'d', '\g<1> would')
    ]
    self._replacement_patterns = [(re.compile(regex, flags=re.IGNORECASE), repl)
                                  for (regex, repl) in replacement_patterns]
  def __call__(self, text):
    for (pattern, repl) in self._replacement_patterns:
      text = re.sub(pattern, repl, text)
    return text


# -------------------- Sentence list functions ----------------
@_class_decorator('word_tokenize')
def word_tokenize(sentence, pt_tokenizer=True):
  """Tokenize sentence into words.

  NOTE: Default is `TreebankWordTokenizer`.

  If pt_tokenizer, use `TreebankWordTokenizer`, don't work well for "can't"

  TODO(zcq)
  """
  if pt_tokenizer:
    return nltk_word_tokenize(sentence)
  else:
    return nltk_WP_tokenize(sentence)


# --------------------- Word list functions -------------------
class remove_stop_words(object):
  def __init__(self):
    self.name = 'remove_stop_words'
    self._english_stops = set(stopwords.words('english'))
  def __call__(self, words):
    return [w for w in words if w.lower() not in self._english_stops]


# -------------------------- Word -----------------------------
class word_stem(object):
  def __init__(self):
    self.name = 'word_stem'
    self._support_algorithm = {
      'porter' : PorterStemmer,
      'lancaster' : LancasterStemmer,
    }
  def __call__(self, word, algorithm='porter'):
    """Stemming."""
    if algorithm not in self._support_algorithm:
      raise ValueError("Supported stemming algorithms: %s, but got %s" % (
        str(self._support_algorithm.keys(), algorithm)))
    stemmer = self._support_algorithm[algorithm]()
    return stemmer.stem(word)

class word_lemmatizing(object):
  def __init__(self):
    self.name = word_lemmatizing
    self._lemmatizer = WordNetLemmatizer()
  def __call__(self, word, pos='n'):
    return self._lemmatizer.lemmatize(word, pos=pos)

def replace_repeat_letters(word):
  """Replace repeated letters.
  
  e.g.
  looooooove -> love
  """
  if wordnet.synsets(word):
    return word
  repeat_regexp = re.compile(r'(\w*)(\w)\2(\w*)')
  repl = r'\1\2\3'
  repl_word = repeat_regexp.sub(repl, word)
  if repl_word != word:
    return replace_repeat_letters(word)
  else:
    return repl_word

class correct_spelling(object):
  def __init__(self, dict_name='en', max_dist=2):
    self.name = 'correct_spelling'
    self._spell_dict = enchant.Dict(dict_name)
    self._max_dist = max_dist
  def __call__(self, word):
    if self._spell_dict.check(word):
      return word
    suggestions = self._spell_dict.suggest(word)
    if suggestions and edit_distance(word, suggestions[0]) \
        <= self._max_dist:
      return suggestions[0]
    else:
      return word

