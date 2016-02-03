#!/usr/bin/python

class Pos:
   'Common base class for all pos'
   empCount = 0

   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Pos.empCount += 1
   
   def displayCount(self):
     print "Total Employee %d" % Pos.empCount

   def displayEmployee(self):
      print "Name : ", self.name,  ", Salary: ", self.salary