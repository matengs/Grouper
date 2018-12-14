#!/usr/local/opt/python/libexec/bin/python
# Python location is local... 
#!/usr/bin/python

import sys
import os
from SupportClasses import *
from SupportExcel import *

groups = list()
classes = list()

xls = excel()

# Populate gro
print('\nWorking... Populate xls.groups with %d students from each class with 1st choice'%(xls.firstDraft))
for groupIndex in range(0,len(xls.groups)):
	worker.addStudentsToGroups(xls.groups,xls.classes,groupIndex,0,xls.firstDraft)

print('Working... Populate remaining xls.groups after priority\n')
for priorityIndex in range(0,3):
	for groupIndex in range(0,len(xls.groups)):
		worker.addStudentsToGroups(xls.groups,xls.classes,groupIndex,priorityIndex,-1)

xls.printGroups()
xls.printClasses()

xls.writeResult()