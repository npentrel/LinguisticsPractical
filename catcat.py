#!/usr/bin/python

class Catcat:
   'Common base class for all pos'

   def __init__(self, category, following_categories):
      self.category = category
      self.count = 0
      self.counts_for_categories = {}
      for cat in following_categories:
         if self.counts_for_categories.has_key(cat):
            self.counts_for_categories[cat] += 1
            self.count += 1
         else:
            self.counts_for_categories[cat] = 1
            self.count += 1
      self.probabilities_for_categories = {}
      self.update_probabilities()

   def update_probabilities(self):
      for c in self.counts_for_categories:
         self.probabilities_for_categories[c] = self.prob(self.counts_for_categories[c])

   def prob(self, c):
      return ((1.0*c)/((1.0)*self.count))
   
   def word(self):
      return self.word

   def display(self):
      print "Category %s , overall count %d, followed by %s" %(self.category, self.count, self.probabilities_for_categories)

   def update(self, more_categories):
      for cat in more_categories:
         if self.counts_for_categories.has_key(cat):
            self.counts_for_categories[cat] += 1
            self.count += 1
         else:
            self.counts_for_categories[cat] = 1
      self.update_probabilities()
