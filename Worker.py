#!/usr/local/opt/python/libexec/bin/python
# Python location is local... 

import sys
import os
import string
import random

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
