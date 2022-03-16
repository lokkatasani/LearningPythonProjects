# File: EasterSunday.py
# Student: Lokprabhat R Katasani
# UT EID: lrk646
# Course Name: CS303E
# 
# Date Created: 01/26/2022
# Date Last Modified: 01/28/2022
# Description of Program: This program recieves a year as an input and outputs Easter Sunday's date and month for that year.

#get input
y=int(input("Enter year: "))

#get outputs
a= y%19
b = y//100
c=y%100
d=b//4
e=b%4
g=(8*b+13)//25
h= (19*a+b-d-g+15)%30
j= c//4
k= c%4
m= (a+11*h)//319
r= (2*e+2*j-k-h+m+32)%7
n= (h-m+r+90)//25
p= (h-m+r+n+19)%32

#display output
print("In ", y , " Easter Sunday is on month ", n, " and day " , p)

