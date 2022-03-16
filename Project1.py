# File: Project1.py
# Student: Lokprabhat Katasani
# UT EID: Lrk646
# Course Name: CS303E
# 
# Date:02/27/2022
# Description of Program: This program allows the user to convert betweek english units and metric units.
# This program will not crash if it gets an incorrect input

#define functions for repeated bodies of big text
def conversiontype():
    print()
    print("""------------------------------------------------------------""")
    print()
    print('''Which direction would you like to convert:
   For English to Metric type: 1
   For Metric to English type: 2
   To Quit type:               3''')
    print()
    
def englishunits():
    print('''   For miles type:  1
   For feet type:   2
   For inches type: 3''')
    print()

def metricunits():
    print('''   For kilometers type:  1
   For meters type:      2
   For centimeters type: 3''')
    print()

#print initial introduction text
print("Welcome to the English/Metric conversion utility.")
print()
print("""This utility allows you to convert between English units 
(miles, feet, inches) and metric units (kilometers, meters, 
centimeters).""")


#start a while loop for the program to keep it going until the user exits the program
endcondition = 'false'
while endcondition == 'false':

#first layer while loop gets what type of conversion to do from the user. This section loops until it gets an input or the user ends the program
    codelayer = 0
    while codelayer ==0:
        conversiontype()
        conversioninput = (input('   Input your answer (1, 2 or 3): '))
        print()

#get english to metric units from user (option 1)
#this is in a while loop until the user inputs a proper response
        if conversioninput == '1':
            codelayer = 1
        
            while codelayer ==1:
                print('Select English units to convert to metric equivalent:')
                englishunits()
                englishunitinput = input(('   Choose English units to convert (1, 2 or 3): '))
                print()

                if englishunitinput == '1' or englishunitinput == '2' or englishunitinput == '3': #check if proper response
                    codelayer = 3
                
                    while codelayer ==3:
                        print('Convert to which metric units:')
                        metricunits()
                        metricunitinput = (input('   Choose target metric units (1, 2 or 3): '))
                        print()
                        
                        if metricunitinput == '1' or metricunitinput == '2' or metricunitinput == '3': #check if proper response
                            codelayer = 4 #exits while loop
                        else:   
                            print('ERROR: Answer must be 1, 2 or 3. Try again.')
                            print()#loops back
                            
                else:
                    print()
                    print('ERROR: Answer must be 1, 2 or 3. Try again.')
                    print()#loops back
                    
#get metric to english units from user (option 2)
#this is in a while loop until the user inputs a proper response
        elif conversioninput == '2':
            codelayer = 2
        
            while codelayer == 2:
                print('Select metric units to convert to English equivalent:')
                metricunits()
                metricunitinput = (input('   Choose target metric units (1, 2 or 3): '))
                print()
            
                if metricunitinput == '1' or metricunitinput == '2' or metricunitinput == '3':#check if proper response
                    codelayer = 3

                    while codelayer ==3:
                        print('Convert to which English units:')
                        englishunits()
                        englishunitinput = (input('   Choose English units to convert (1, 2 or 3): '))
                        print()
                    
                        if englishunitinput == '1' or englishunitinput == '2' or englishunitinput == '3':#check if proper response
                            codelayer = 5 #exits while loop
                        else:
                            print('ERROR: Answer must be 1, 2 or 3. Try again.')
                            print()#loops back
                        
                else:
                    print('ERROR: Answer must be 1, 2 or 3. Try again.')
                    print()#loops back
        
#option 3 ends the program by changing the endcondition variable to true         
        elif conversioninput == '3':
            print('Thanks for using our converter. Goodbye!')
            codelayer =6
            endcondition = 'true'
            
#if the input is not proper
        else:
            print('ERROR: Answer must be 1, 2 or 3. Try again.') #loops back

#this section sets the variables: metric, metric_covfactor, english, english_covfactor based on the user inputs      
    if codelayer != 6:
        meter2feet= 3.28084  
        if  metricunitinput == '1':
            metric = 'kilometers'
            metric_covfactor = 1000
        elif  metricunitinput == '2':
            metric = 'meters'
            metric_covfactor = 1
        elif  metricunitinput == '3':
            metric = 'centimeters'
            metric_covfactor = (1/100)
           
        if  englishunitinput == '1':
            english = 'miles'
            english_covfactor = (5280)
        elif  englishunitinput == '2':
            english = 'feet'
            english_covfactor = 1
        elif  englishunitinput == '3':
            english = 'inches'
            english_covfactor = 1/12

#english to metric
    if codelayer == 4:
        
#get number to convert
        str1 = ("Enter the number of "+ english + " to convert to "+ metric + ": ")
        number = eval(input(str1))
        print()
        
#convert the number
        result = (number)*(english_covfactor)*(1/meter2feet)*(1/metric_covfactor)
        
#print the result
        print("RESULT: " + str(float(number)) + " " + english + " = " + str(format(result, '.3f')) +  " " + metric)


#metric to english
    if codelayer == 5:
        
#get number to convert
        str1 = ("Enter the number of "+ metric + " to convert to "+ english + ": ")
        number = eval(input(str1))
        print()
        
#convert the number
        result = (number)*(metric_covfactor)*(meter2feet)*(1/english_covfactor)
        
#prin the result
        print("RESULT: " + str(float(number)) + " " + metric + " = " + str(format(result,'.3f')) + " " +english)
     
    

