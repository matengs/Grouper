#!/usr/local/opt/python/libexec/bin/python

import sys
import os
import glob
from SupportClasses import *
import xlrd
import xlwt


class excel:
	def __init__(self):
		self.path = os.getcwd()
		self.groupFile = self.getGroupFile()
		self.classFiles = self.getClassFiles()
		self.createGroups()
		self.createClasses()
		self.print()
	def getGroupFile(self):
		fName = glob.glob('Gr*.xls*')
		if not fName:
			print('ERROR: Can not find a group excel file in %s'%(self.path))
			sys.exit()
		fName = os.path.abspath(fName[0])
		if os.path.isfile(fName):
			return fName
		else:
			print('ERROR: Can not read %s'%(fName))
			sys.exit()
	def getClassFiles(self):
		fNames = glob.glob('Kl*.xls*')
		ans = list()
		if not fNames:
			print('ERROR: Can not find any school class excel files in %s'%(self.path))
		for fName in fNames:
			if os.path.isfile(fName):
				ans.append(os.path.abspath(fName))
			else: 
				print('ERROR: Can not read %s'%(fName))
				sys.exit()
		return ans
	def createGroups(self):
		wb = xlrd.open_workbook(self.groupFile)
		indexCol = 0
		nameCol = 1
		capacityCol = 2
		groups = list()
		for sheet in wb.sheets():
			nRows = sheet.nrows
			nCols = sheet.ncols
			for row in range(1, nRows):
				groups.append(sGroup(int(sheet.cell(row,indexCol).value),str(sheet.cell(row,nameCol).value),int(sheet.cell(row,capacityCol).value)))
		self.groups = groups
	def createClasses(self):
		classes = list()
		classIndex=0
		for fName in self.classFiles:
			wb = xlrd.open_workbook(fName)
			nameCol = 0
			className = os.path.splitext(os.path.basename(fName))[0]
			students = list()
			for sheet in wb.sheets():
				nRows = sheet.nrows
				nCols = sheet.ncols
				currentClass = sClass(classIndex,className,nRows-1)
				for row in range(1, nRows):
					groupSelect = list()
					for col in range(1,nCols):
						groupSelect.append(int(sheet.cell(row,col).value))
					currentClass.students.append(student(classIndex,className,str(sheet.cell(row,nameCol).value),groupSelect))
			self.nGroupSelect = len(groupSelect)
			classes.append(currentClass)
			classIndex+=1
		self.classes = classes
	def	writeResult(self):
		wb = xlwt.Workbook()
		fName = os.path.join(self.path,'Result.xls')
		for group in self.groups:
			sheet = wb.add_sheet(group.name)
			sheet.write(0,0,group.name)
			sheet.write(1,0,'Class')
			sheet.write(1,1,'Name')
			for i in range(2,self.nGroupSelect+2):
				sheet.write(1,i,'Group')
			rowOffset = 2
			i=0
			for student in group.students:
				sheet.write(rowOffset+i,0,student.sClassName)
				sheet.write(rowOffset+i,1,student.name)
				offsetCol = 2
				j=0
				for groupSelection in student.groups:
					sheet.write(rowOffset+i,offsetCol+j,groupSelection)
					j+=1
				i+=1
		sheet = wb.add_sheet('No group')
		sheet.write(0,0,'No group')
		sheet.write(1,0,'Class')
		sheet.write(1,1,'Name')
		for i in range(2,self.nGroupSelect+2):
			sheet.write(1,i,'Group')
		rowOffset = 2
		wb.save(fName)
	def print(self):
		print('Group file:\n - %s'%(self.groupFile))
		print('Class files:')
		for fName in self.classFiles:
			print(' - %s'%(fName))
		printGroups(self.groups)
		printClasses(self.classes)

xls = excel()