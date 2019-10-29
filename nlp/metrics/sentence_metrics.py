"""Evaluation of a sentence."""

from lingua.nlp.embedding.word2vec import W2VModel, \
  GooglePretrainedW2V


class SentenceMetrics(object):
  """Base class for sentence metrics."""


class SentenceIntegrity(SentenceMetrics):
  """Evaluate integrity of a sentence."""
  
  def eval(self, input_text):
    raise NotImplementedError()


class W2CSentenceIntegrity(SentenceIntegrity):
  """Use pretrained word2vec model to eval sentence integrity."""
  def __init__(self, w2vmodel,
               num_pred_words=5,
               window=5):
    """Evaluate sentence integrity using a pretrained model.

    Parameters
    ----------
    w2vmodel : `W2VModel` or str
      Pretrained word2vec model.
    num_pred_words : int
      Used in `predict_output_word` as topn parameter.
    window : int
      The window length, if 0, means window = lenght of word_list.
    """
    if isinstance(w2vmodel, str):
      # Assume a google pretrained model.
      w2vmodel = GooglePretrainedW2V(w2vmodel)
    if not isinstance(w2vmodel, W2VModel):
      raise ValueError("w2v should be str of W2VModel, but got %s"
                       % type(w2vmodel))
    self._model = w2vmodel
    self._num_pred_words = num_pred_words
    if window and window % 2 != 1:
      raise ValueError("window should be odd to make sure there is one "
                       "center word, but got %d" % window)
    self._window = window

  def eval(self, input_text):
    if not isinstance(input_text, str):
      raise ValueError("str excepted, but got %s" % type(input_text))

    word_prob_list =  self._model.model.predict_output_word(
                          context_words_list, self._num_pred_words)


