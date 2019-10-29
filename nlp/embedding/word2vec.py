# -*- coding:utf-8 -*-

"""Word2vec model."""

import gensim


class W2VModel(object):
  """Base class for word2vec model."""


class GooglePretrainedW2V(W2VModel):
  """Google pretrained word2vec model, load by gensim.
  """
  def __init__(self,
               model_path='./model/GoogleNews-vectors-negative300.bin'):
    self._model_path = model_path
  
  def load_model(self):
    # Load Google's pre-trained Word2Vec model.
    self._model = gensim.models.Word2Vec.load_word2vec_format(
                      self._model_path, binary=True)

  @property
  def model(self):
    return self._model