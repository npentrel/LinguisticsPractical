#!/usr/bin/python
import re

def word_pos2(word):
   allmatches = re.findall("/[^/]*$", word, re.DOTALL)
   pos = allmatches[0]
   return pos[1:]

class Pos:
   'Common base class for all pos'

   def __init__(self, word, following_words, occurrences):
      self.word = word
      self.following_words = following_words
      self.occurrences = occurrences
   
   def word(self):
      return self.word

   def following_categories(self):
      categories = map(word_pos2, self.following_words)
      return categories

   def word_pos(self):
      allmatches = re.findall("/[^/]*$", self.word, re.DOTALL)
      pos = allmatches[0]
      return pos[1:]

   def display(self):
     print "Pos %s , %s , followed by %s, used: %d" %(self.word, self.word_pos(), sorted(self.following_words), self.occurrences)

   def update(self, word, next_word):
      self.occurrences += 1
      if not next_word is "" :
         self.following_words.extend([next_word])
