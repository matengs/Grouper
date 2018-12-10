#!/usr/local/opt/python/libexec/bin/python
# Python location is local... 

import sys
import os
import random
import string
#from random import randint

class student:
	def __init__(self,sClassName,sName,sGroups):
		self.sClass = sClassName
		self.name = sName
		self.groups = sGroups
	def getSelection(self):
		return self.groups[0]



class sClass:
	def __init__(self,name,capacity):
		self.name = name
		self.capacity = capacity
		self.students = list()
	def simSetup(self):
		for _ in range(self.capacity):
			sName = ''.join(random.choices(string.ascii_uppercase, k=8))
			sSelection = random.sample(range(1,11),3)
			self.students.append( student(self.name,sName,sSelection) )
	def printPopulation(self):
		for student in self.students:

			print(' - %s %s top sel.: %d'%(student.name,str(student.groups),student.getSelection()))

