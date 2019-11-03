# -*- coding:utf-8 -*-
import sys
sys.path.insert(0, '../../../')
import re
from functools import partial

from lingua.nlp.preprocess.utils import remove_pattern, \
    remove_single_letter_words, replace_abbr_not, \
    replace_repeat_letters, correct_spelling
from lingua.nlp.preprocess.processor_ins import WordLevelProcessor


def get_imdb_review(
    path='../../data/imdb/liulangdiqiu_imdb_review.txt'):
  """Parse reviews from copied txt from website.

  Patterns:
    score \n title \n author date \n review \n Permalink
  """
  with open(path, 'r') as f:
    text = f.read()
  text_list = re.split(r'\nPermalink\n', text)
  authors = []
  date = []
  review = []
  title = []
  scores = []
  for sample in text_list:
    sample = sample.strip().split('\n')
    if re.search(r'\d/10', sample[0]):
      i = 1
      scores.append(float(sample[0].strip().split('/')[0]) / 10)
    else:
      scores.append(-1)
      i = 0
    title.append(sample[i])
    authors.append(sample[i + 1].split()[0])
    date.append(' '.join(sample[i + 1].split()[1:]))
    cur_review = []
    for r in sample[(i + 2):]:
      if 'Sign in to vote' in r:
        continue
      if not len(r) > 2:
        continue
      else:
        cur_review.append(r)
    review.append('\n'.join(cur_review))
  return authors, date, title, scores, review

def get_youtube_review(
    path='../../data/imdb/liulangdiqiu_youtube_review.txt'):
  """Parse reviews from youtube.
  
  Patterns:
    前|过）\n review \n\n+
  """
  with open(path, 'r') as f:
    text = f.read()
  text_list = re.split(r'前\n|过）\n', text)[1:]
  review = []
  for sample in text_list:
    review_sample = re.split(r'\n\n+(回复|\d\n)', sample)[0]
    review_sample = remove_pattern()(review_sample, r'\n+\d+$')
    review_sample = remove_pattern()(review_sample, r'\n+展开$')
    review.append(review_sample)
  return review


if __name__ == '__main__':
  youtube_review = get_youtube_review()
  _, _, _, _, imdb_review = get_imdb_review()

  remove_new_line = partial(re.sub, r'\n\n+', '\n')

  with open('lldq_youtube_review.txt', 'w') as f:
    for r in youtube_review:
      r = remove_new_line(r).strip()
      r = replace_abbr_not()(r)
      r = r.replace('Permalink', '')
      r = r.replace('\n', ' ')
      # r = r.replace('sci-fi', 'science fiction')
      f.write(r + '\n\n')
  
  with open('lldq_imdb_review.txt', 'w') as f:
    for r in imdb_review:
      r = r.replace('Warning: Spoilers', '')
      r = replace_abbr_not()(r)
      r = remove_new_line(r).strip()
      r = r.replace('\n', ' ')
      # r = r.replace('sci-fi', 'science fiction')
      f.write(r + '\n\n')


  # TODO(zcq) 评论里有很多特殊单词，例如 sci-fi, emoji表情, OMG, LOL, btw, 其他语言

  # review_processor = WordLevelProcessor()


