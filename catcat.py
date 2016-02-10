#!/usr/bin/python

class Catcat:
   'Common base class for all pos'

   def __init__(self, category, following_categories):
      self.category = category
      self.probs_for_categories = {}
      for cat in following_categories:
         if self.probs_for_categories.has_key(cat):
            self.probs_for_categories[cat] += 1
         else:
            self.probs_for_categories[cat] = 1
   
   def word(self):
      return self.word

   def display(self):
      print "Category %s , followed by %s" %(self.category, self.probs_for_categories)

   def update(self, more_categories):
      for cat in more_categories:
         if self.probs_for_categories.has_key(cat):
            self.probs_for_categories[cat] += 1
         else:
            self.probs_for_categories[cat] = 1
