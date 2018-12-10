#!/usr/local/opt/python/libexec/bin/python
# Python location is local... 

import sys
import os


class sGroup:
	def __init__(self,index,name,capacity):
		self.index = index
		self.name = name
		self.capacity = capacity
		self.memembers = 0
		self.students = list()
	def printStatus(self):
		print('%s capacity: %d'%(self.name,self.capacity))
		print(' - index: %d'%self.index)
		print(' - members: %d'%self.members)

