# File: MinMax-1.py
# Student: Lokprabhat Katasani
# UT EID: LRK646
# Course Name: CS303E
# 
# Date: 2/25/2022
# Description of Program: This program accepts any number of integer inputs
# and prints out the maximum and minimum number from the inputs. The program
# ends when "stop" is inputed. It also displays "You didn't enter any numbers"
# when not given an input


#get inital input
num = input("Enter an integer or 'stop' to end: ")

#initialize variables
maximum = None
minimum = None

#if first input isn't stop, set max and min to that number
if num != "stop":
        maximum = int(num)
        minimum = int(num)

#continue the loop and ask for another input
while num != "stop":
    num = input("Enter an integer or 'stop' to end: ")

    #check if this next input is new max or min
    if num != "stop":
        num = int(num)
        if num < minimum:
            minimum = num
        elif num >maximum:
            maximum = num

#display outputs
#check to make sure numbers where inputted
if maximum == None:
    print("You didn't enter any numbers")
else:
    print("The maximum is", maximum)
    print("The minimum is", minimum)
 
    



