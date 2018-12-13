#!/usr/local/opt/python/libexec/bin/python
# Python location is local... 

import sys
import os


class sGroup:
	def __init__(self,index,name,capacity):
		self.index = index
		self.name = name
		self.capacity = capacity
		self.n = 0
		self.students = list()
	def printStatus(self):
		print('%s (index: %d capacity: %d n: %d open: %d)'%(self.name,self.index,self.capacity,self.n,self.getOpenSlots()))
	def printPopulation(self):
		for student in self.students:
			student.print()
	def getOpenSlots(self):
		ans = self.capacity-self.n
		if ans>0:
			return ans
		else:
			return 0
	def addStudents(self,students):
		self.n+=len(students)
		self.students.extend(students)
	def addStudent(self,student):
		self.n+=1
		self.students.append(student)
