#!/usr/bin/python

class Pos:
   'Common base class for all pos'

   def __init__(self, word, following_words, occurrences):
      self.word = word
      self.following_words = following_words
      self.occurrences = occurrences
   
   def display(self):
     print "Pos %s , followed by %s, used: %d" %(self.word, sorted(self.following_words), self.occurrences)

   def update(self, word, next_word):
      self.occurrences += 1
      if not next_word is "" :
         self.following_words.extend([next_word])
