import sys
import os
import random
import string

class worker:
	def __init__(self):
		print('Initialize worker')
	def addStudentsToGroups(groups,classes,groupIndex,level,n=-1):
		ans=list()
		# Select students from all classes
		for sClass in classes:
			ans.extend(sClass.getStudents(groupIndex,level,n))
		if (len(ans)>groups[groupIndex].getOpenSlots()):
			randSelection = random.sample(range(0,len(ans)),groups[groupIndex].getOpenSlots())
			randSelection.sort(reverse=True)
			for i in randSelection:
				groups[groupIndex].addStudent(ans.pop(i))
			for student in ans:
				classes[student.sClassIndex].students.append(student)
		else:
			groups[groupIndex].addStudents(ans)

# Group Class
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
		self.sortStudents()
	def addStudent(self,student):
		self.n+=1
		self.students.append(student)
		self.sortStudents()
	def sortStudents(self):
		self.students.sort(key=lambda x: x.sClassIndex, reverse=False)

# Student Class
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

# School class Class
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
		# Return the unfortunate and update 
		self.students = miss
		self.n=len(self.students)
		return hit

