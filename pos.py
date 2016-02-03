#!/usr/bin/python

class Pos:
   'Common base class for all pos'

   def __init__(self, word, following_words, occurrences):
      self.word = word
      self.following_words = following_words
      self.occurrences = occurrences
   
   def display(self):
     print "Pos %s , followed by %s, used: %d" %(self.word, self.following_words, self.occurrences)
