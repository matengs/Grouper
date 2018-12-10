#!/usr/bin/python

#!/usr/local/opt/python/libexec/bin/python
# Python location is local... 

import sys
import os
from sClass import *
from sGroup import sGroup

groups = list()
classes = list()

# Setup groups
for i in range(0,10):
	groups.append(sGroup(i,'G_'+chr(97+i),10))

# Setup Classes
for i in range(0,6):
	classes.append(sClass('C_'+chr(97+i),8))
for currentClass in classes:
	currentClass.simSetup()

# Print 
print('\nGROUPS:')
for group in groups:
	print(group.name+' capacity: '+str(group.capacity)+' index: '+str(group.index))

print('\nCLASSES')
for currentClass in classes:
	print(currentClass.name+' (Capacity: '+str(currentClass.capacity)+')')
	currentClass.printPopulation()
####

