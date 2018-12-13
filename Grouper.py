#!/usr/local/opt/python/libexec/bin/python
# Python location is local... 
#!/usr/bin/python

import sys
import os
from SupportClasses import *



########## MAIN #############
groups = list()
classes = list()

nGroups = 10
nGroupsCapacity = 20
nClasses = 6
nStudents = 30
firstDraft = 3

# Setup groups/classes
for i in range(0,nGroups):
	groups.append(sGroup(i,'G_'+chr(97+i),nGroupsCapacity))
for i in range(0,nClasses):
	classes.append(sClass(i,'C_'+chr(97+i),nStudents))
for currentClass in classes:
	currentClass.simSetup(nGroups)

printGroups(groups)
printClasses(classes)

# Populate gro
print('\nPopulate groups with %d students from each class with 1st choice'%(firstDraft))
for groupIndex in range(0,nGroups):
	worker.addStudentsToGroups(groups,classes,groupIndex,0,firstDraft)

print('Populate remaining groups after priority')
for priorityIndex in range(0,3):
	for groupIndex in range(0,nGroups):
		worker.addStudentsToGroups(groups,classes,groupIndex,priorityIndex,-1)

printGroups(groups)
printClasses(classes)