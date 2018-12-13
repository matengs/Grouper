#!/usr/local/opt/python/libexec/bin/python
# Python location is local... 

import sys
import os
import random
import string

class student:
	def __init__(self,sClassIndex,sClassName,sName,sGroups):
		self.sClassIndex = sClassIndex
		self.sClassName = sClassName
		self.name = sName
		self.groups = sGroups
	def getSelection(self,level=0):
		return self.groups[level]
	def print(self):
		print('%d %s %s %s'%(self.sClassIndex,self.sClassName,self.name,str(self.groups)))


class sClass:
	def __init__(self,index,name,n):
		self.index = index
		self.name = name
		self.n = n;
		self.students = list()
	def simSetup(self,nGroups):
		for _ in range(self.n):
			sName = ''.join(random.choices(string.ascii_uppercase, k=8))
			sSelection = random.sample(range(0,nGroups),3)
			self.students.append( student(self.index,self.name,sName,sSelection) )

	def printPopulation(self):
		for student in self.students:
			print(' - %s %s'%(student.name,str(student.groups)))
	def getStudents(self,group,level=0,n=-1):
		hit = list()
		miss = list()
		# Select those who match
		for student in self.students:
			if group == student.getSelection(level):
				hit.append(student)
			else:
				miss.append(student)
		# Do we only pick a limited number?
		if (n>0) and (len(hit)>n):
			randSelection = random.sample(range(0,len(hit)),n)
			randSelection.sort(reverse=True)
			tmp = list()
			for i in randSelection:
				tmp.append(hit.pop(i))
			miss.extend(hit)
			hit = tmp

		self.students = miss
		self.n=len(self.students)

		return hit

