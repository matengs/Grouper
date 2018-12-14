#!/usr/local/opt/python/libexec/bin/python
# Python location is local... 
#!/usr/bin/python

import sys
import os
from SupportClasses import *
from SupportExcel import *


########## MAIN #############
groups = list()
classes = list()


firstDraft = 3
userFirstDraft = input('How many should get their first choice? ')
if userFirstDraft:
	firstDraft = int(userFirstDraft)

# SIMULATION CODE
# Setup groups/classes
# nGroups = 10
# nGroupsCapacity = 20
# nClasses = 6
# nStudents = 30
# for i in range(0,nGroups):
# 	groups.append(sGroup(i,'G_'+chr(97+i),nGroupsCapacity))
# for i in range(0,nClasses):
#	classes.append(sClass(i,'C_'+chr(97+i),nStudents))
# for currentClass in classes:
# 	currentClass.simSetup(nGroups)

xls = excel()

printGroups(xls.groups)
printClasses(xls.classes)

# Populate gro
print('\nPopulate xls.groups with %d students from each class with 1st choice'%(firstDraft))
for groupIndex in range(0,len(xls.groups)):
	worker.addStudentsToGroups(xls.groups,xls.classes,groupIndex,0,firstDraft)

print('Populate remaining xls.groups after priority')
for priorityIndex in range(0,3):
	for groupIndex in range(0,len(xls.groups)):
		worker.addStudentsToGroups(xls.groups,xls.classes,groupIndex,priorityIndex,-1)

printGroups(xls.groups)
printClasses(xls.classes)