

from gensim.models import Phrases
# from gensim.models.phrases import Phraser as Phrases
from gensim.corpora import Dictionary
from gensim.models import LdaModel


class LDAModelWrapper(object):
  """LDA model class."""
  def __init__(self, min_count=20,
               no_below=1,
               no_above=0.2,
               num_topics=10,
               chunksize=2000,
               passes=20,
               iterations=400,
               eval_every=None,
               verbose=True):
    """
    Parameters
    ----------

    no_below : int
      Keep tokens which are contained in at least no_below documents.
    no_above : float
      Keep tokens which are contained in no more than no_above documents
      (fraction of total corpus size, not an absolute number).


    chunksize : int
      chunksize controls how many documents are processed at a time 
      in the training algorithm. Increasing chunksize will speed up training,
      at least as long as the chunk of documents easily fit into memory.
      I’ve set chunksize = 2000, which is more than the amount of documents,
      so I process all the data in one go. Chunksize can however influence the
      quality of the model, as discussed in Hoffman and co-authors [2],
      but the difference was not substantial in this case.

    passes : int
      If you set passes = 20 you will see this line 20 times. 
      Make sure that by the final passes, most of the documents have converged.
      So you want to choose both passes and iterations to be 
      high enough for this to happen.
    """
    
    self._min_count = min_count
    self._no_below = no_below
    self._no_above = no_above

    # Set training parameters.
    self._num_topics = num_topics
    self._chunksize = chunksize
    self._passes = passes
    self._iterations = iterations
    self._eval_every = eval_every
    self._verbose = verbose

  def preprocess(self, docs):
    bigram = Phrases(docs, min_count=self._min_count)
    for idx in range(len(docs)):
      for token in bigram[docs[idx]]:
        if '_' in token:
          # Token is a bigram, add to document.
          docs[idx].append(token)
    # Create a dictionary representation of the documents.
    dictionary = Dictionary(docs)
    # Filter out words
    dictionary.filter_extremes(no_below=self._no_below, 
        no_above=self._no_above)
    # Bag-of-words representation of the documents.
    corpus = [dictionary.doc2bow(doc) for doc in docs]
    self._corpus = corpus
    self._dictionary = dictionary
    if self._verbose:
      print('Number of unique tokens: %d' % len(dictionary))
      print('Number of documents: %d' % len(corpus))


  def train(self):
    # Make a index to word dictionary.
    temp = self._dictionary[0]  # This is only to "load" the dictionary.
    id2word = self._dictionary.id2token

    # We set alpha = 'auto' and eta = 'auto'. Again this is somewhat technical,
    # but essentially we are automatically learning two parameters in the model
    # that we usually would have to specify explicitly.

    self._model = LdaModel(
        corpus=self._corpus,
        id2word=id2word,
        chunksize=self._chunksize,
        alpha='auto',
        eta='auto',
        iterations=self._iterations,
        num_topics=self._num_topics,
        passes=self._passes,
        eval_every=self._eval_every
    )
  
  def get_topics(self):
    top_topics = self._model.top_topics(self._corpus)

    # Average topic coherence is the sum of topic coherences of all topics,
    # divided by the number of topics.
    avg_topic_coherence = sum([t[1] for t in top_topics]) / self._num_topics
    print('Average topic coherence: %.4f.' % avg_topic_coherence)

    if self._verbose:
      from pprint import pprint
      pprint(top_topics)

