# File: Student.py
# Student: Lokprabhat R Katasani
# UT EID: LRK66
# Course Name: CS303E
# 
# Date:02/15/2022
# Description of Program: This program defines a student object that contains their first 2 exam scores and their name. This class can also display all the
# information that it has along with change it. Viewing and changing the data is operated using the set and get commands. Finally this program also displays
# the average of their test scores.

class Student:

    def __init__(self,name, exam1= None, exam2= None): # when defineing a student the exam scores might not be given, so initialize them to None
        #set each variable to the individual object
        self.name = name
        self.exam1 = exam1
        self.exam2 = exam2

    def __str__(self):
        #create a string with each information piece on a different line
        outputstr = str('Student: {}\n'.format(self.name)) +  str('  Exam1: {}\n'.format(self.exam1)) + str('  Exam2: {}'.format(self.exam2))
        return outputstr
   
    def getName(self):
        #display the name
        return self.name

    def getExam1Grade(self):
        if self.exam1 == None: # do nothing if there is no exam 1 grade
            pass
        else:
            return self.exam1 # display the grade if there is one

    def getExam2Grade(self):
        if exam2 == None: # do nothing if there is no exam 2 grade
            pass
        else:
            return self.exam2 # display the grade if there is one
    
    def setExam1Grade(self, exam1):
        self.exam1 = exam1 #update the grade
        
    def setExam2Grade(self, exam2):
        self.exam2 = exam2 #update the grade

    def getAverage(self):
        if self.exam1 != None and self.exam2 != None: # check that there are 2 grades given
            return (self.exam1+self.exam2)/2 #display average
        else:
            print('Some exam grades are not available.') #if there are not 2 grades given
            
