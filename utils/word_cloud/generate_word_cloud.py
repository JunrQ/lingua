# -*- coding:utf-8 -*-
import sys
sys.path.insert(0, '../../')
import os


from lingua.utils.word_cloud import WordCloud

if __name__ == '__main__':
  wc = WordCloud()
  parent_path = '/Users/junr/Documents/git/lingua/data/20191119-word-cloud/'
  file_name = [os.path.join(parent_path, x) 
               for x in os.listdir(parent_path) if x.endswith('txt')]
  for f in file_name:
    # TODO
    output_name = f.split('.txt')[0] + '.png'
    wc.add_file(f)
    wc.generate_word_cloud(output_name)
