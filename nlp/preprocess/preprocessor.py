"""Preprocessor for NLP."""



class Processor(object):
  """BaseProcessor class.
  """
  def __init__(self):
    self._funcs = []
  
  def add_func(self, func):
    self._funcs.append(func)

  def __call__(self, input):
    for f in self._funcs:
      input = f(input)
    return input

class TextProcessor(Processor):
  def __call__(self, input):
    if not isinstance(input, str):
      raise ValueError("Only support input string, but got %s" % type(input))
    return super(TextProcessor, self).__call__(input)


class ListProcessor(Processor):
  def __call__(self, input):
    if not isinstance(input, list):
      raise ValueError("Only support input list, but got %s" % type(input))
    return super(TextProcessor, self).__call__(input)









