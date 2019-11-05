

import os
from xml.dom.minidom import parse

def orangize(path, output_csv):
  csv_file = open(output_csv, 'w')
  for txt in os.listdir(path):
    if txt.endswith('.txt'):
      txt_path = os.path.join(path, txt)
      senti_result = txt_path + '.xml'

      with open(txt_path, 'r') as f:
        review = f.read().strip()
        msg = txt
      dom_tree = parse(senti_result)
      # root
      collection = dom_tree.documentElement
      sentences = collection.getElementsByTagName('sentences')[0]
      sentences = sentences.getElementsByTagName('sentence')
      if len(sentences) < 1:
        continue
      for sentence_element in sentences:
        senti_value = sentence_element.getAttribute('sentimentValue')
        senti = sentence_element.getAttribute('sentiment')
        msg += ',%s,%s' % (senti, senti_value)
      # import pdb; pdb.set_trace()
      csv_file.write(msg + '\n')
  csv_file.close()

if __name__ == '__main__':
  orangize('imdb_sentiment_analysis', 'imdb_sentiment_analysis.csv')
  orangize('youtube_sentiment_analysis', 'youtube_sentiment_analysis.csv')

