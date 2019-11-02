"""Preprocessor for NLP."""


class Processor(object):
  """BaseProcessor class.
  """
  def __init__(self):
    self._funcs = []
  
  def add_func(self, func):
    if isinstance(func, list):
      for f in func:
        self._funcs.append(f)
    else:
      self._funcs.append(func)

  def __call__(self, input, debug=False):
    for f in self._funcs:
      output = f(input)
      if debug:
        print("[%s]\n[before] %s\n[after] %s" % (
          'noname' if not hasattr(f, 'name') else f.name,
          str(input),
          str(output)
        ))
      input = output
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

