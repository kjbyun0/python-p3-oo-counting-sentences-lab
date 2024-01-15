#!/usr/bin/env python3

class MyString:
  def __init__(self, value=''):
    self.value = value

  @property
  def value(self):
    return self._value
  
  @value.setter
  def value(self, value):
    if isinstance(value, str):
      self._value = value
    else:
      print('The value must be a string.')

  def is_end_with(self, ch):
    if self.value[-1] == ch:
      return True
    return False

  def is_sentence(self):
    return self.is_end_with('.')
  
  def is_question(self):
    return self.is_end_with('?')
  
  def is_exclamation(self):
    return self.is_end_with('!')
  
  def count_sentences(self):
    tmp = self.value.replace('?', '.')
    tmp = tmp.replace('!', '.')
    sentences = tmp.split('.')
    return len([sentence for sentence in sentences if sentence != ''])

  

  


