import re
import nltk
from nltk.tokenize import sent_tokenize as nltk_sent_tokenize, \
    word_tokenize as nltk_word_tokenize, WordPunctTokenizer as nltk_WP_tokenize, \
    PunktWordTokenizer as nltk_PW_tokenize
from nltk.corpus import stopwords

# https://github.com/vasisouv/tweets-preprocessor/blob/master/twitter_preprocessor.py

def get_single_letter_words_pattern():
  return re.compile(r'(?<![\w\-])\w(?![\w\-])')





# ---------------------- Text functions -----------------------
def sentence_tokenize(text):
  """Tokenize text into sentences."""
  return nltk_sent_tokenize(text)






# -------------------- Sentence list functions ----------------
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
def remove_stop_words(words):
  english_stops = set(stopwords.words('english'))
  return [w for w in words if w.lower() not in english_stops]





