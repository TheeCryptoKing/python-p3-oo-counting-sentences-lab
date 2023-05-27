#!/usr/bin/env python3

class MyString:
  def __init__(self, value=''):
    self.value = value

  # dont foget get_ for a property/child function
  def get_value(self):
    return self._value 
  
  def set_value(self, value):
    if isinstance(value, str):
      self._value = value
    else: 
      print('The value must be a string.')

  value = property(get_value, set_value)

  def is_sentence(self):
      # dont get to complicated with loops, look at what you are return
      if self.value.count('.') >= 1:
        return True
      else: 
        return False
      # return value.endswith('.')

  def is_question(self):
    if self.value.count('?'):
      return True 
    else: 
      return False
    # return value.endswith('?')

  def is_exclamation(self):
    if self.value.count('!'):
      return True 
    else: 
      return False
    # return value.endswith('!')

  def count_sentences(self):
    # split and endswith or -1
    #-1 is more index and one of the things we have to master
    # can use count to count all sentences
    # add to some of of counter 
    # either seperate sentences and count
    # or count all snetences simultaneously 
    # sentences = 0
    # for x in self.value.split(" "):
    #   if x.count('.') > 0:
    #     sentences += 1
    #   elif x.count('?') > 0:
    #     sentences += 1
    #   elif x.count('!') > 0:
    #     sentences += 1
    #   return sentences 
    # ends with and split work better becasue the dont count the out right number of !, . , and ? only the ones that end in a sentence
    counter = 0 
    sentences = self.value.split(" ")
    for word in sentences:
        if word and word[-1] in ('.', '?', '!'):
            counter += 1
    return counter

# can also use 
#  if word.endswith(('.', '?', '!')):
#             counter += 1
    

devon = MyString("This, well, is a sentence. This is too!! And so is this, I think? Woo...")
print(devon.count_sentences())


