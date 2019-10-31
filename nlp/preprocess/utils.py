import re
import nltk
from nltk.tokenize import sent_tokenize as nltk_sent_tokenize, \
    word_tokenize as nltk_word_tokenize, WordPunctTokenizer as nltk_WP_tokenize, \
    PunktWordTokenizer as nltk_PW_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, LancasterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
from nltk.metrics import edit_distance
import enchant


def _class_decorator(name):
  # Make a function a class
  # TODO(zcq) May loss doc.
  def _func_decorator(func):
    def _wrapper(self, *args, **kwrags):
      return func(*args, **kwrags)
    C = type(name, (object, ),
            {'__call__' : _wrapper})
    return C
  return _func_decorator
    

@_class_decorator('get_single_letter_words_pattern')
def get_single_letter_words_pattern():
  return re.compile(r'(?<![\w\-])\w(?![\w\-])')


# ---------------------- Text functions -----------------------
@_class_decorator('sentence_tokenize')
def sentence_tokenize(text):
  """Tokenize text into sentences."""
  return nltk_sent_tokenize(text)

class replace_abbr_not(object):
  """Replace '

  e.g.
  can't -> cannot
  i'm -> i am
  """
  def __init__(self):
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
    self._replacement_patterns = [(re.compile(regex), repl) for 
                                  (regex, repl) in replacement_patterns]
  def __call__(self, text):
    for (pattern, repl) in self._replacement_patterns:
      text = re.sub(pattern, repl, text)
    return text






# -------------------- Sentence list functions ----------------
@_class_decorator('word_tokenize')
def word_tokenize(sentence, pt_tokenizer=True, separate_punc=True):
  """Tokenize sentence into words.

  NOTE: Default is `TreebankWordTokenizer`.

  If pt_tokenizer, use `TreebankWordTokenizer`, don't work well for "can't"
  If separate_punc, use `WordPunctTokenizer`
  If not separate_punc, use `PunktWordTokenizer`

  TODO(zcq)
  """
  if pt_tokenizer:
    return nltk_word_tokenize(sentence)
  if separate_punc:
    return nltk_WP_tokenize(sentence)
  else:
    return nltk_PW_tokenize(sentence)



# --------------------- Word list functions -------------------
class remove_stop_words(object):
  def __init__(self):
    self._english_stops = set(stopwords.words('english'))
  def __call__(self, words):
    return [w for w in words if w.lower() not in self._english_stops]




# -------------------------- Word -----------------------------
class word_stem(object):
  def __init__(self):
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




