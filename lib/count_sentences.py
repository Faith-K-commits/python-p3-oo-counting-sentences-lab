#!/usr/bin/env python3

class MyString:
  def __init__(self, value=''):
      self._value = value
    
  @property
  def value(self):
    return self._value
  
  @value.setter
  def value(self, new_value):
    if isinstance(new_value, str):
      self._value = new_value
    else:
      print("The value must be a string.")
  
  def is_sentence(self):
    return self._value.endswith(".")
  
  def is_question(self):
    return self._value.endswith("?")
  
  def is_exclamation(self):
    return self._value.endswith("!")
  
  def count_sentences(self):
      if not self._value.strip():
          return 0
      import re
      sentences = re.split(r'[.!?]', self._value)
      sentences = [s for s in sentences if s.strip()]
      return len(sentences)