# File: Payroll.py
# Student: Lokprabhat R Katasani
# UT EID: LRK646
# Course Name: CS303E
# 
# Date:02/08/2022
# Description of Program: Inputting payroll information into this program
# outputs a payroll statement that includes the following information:
# name, hours worked, payrate, gross pay, deductions, and net pay

#Get inputs
name = input("Enter employee's name: ")
hours = float(input("Enter number of hours worked in a week: "))
payrate = float(input("Enter hourly pay rate: "))
ftax = float(input("Enter federal tax withholding rate: "))
stax = float(input("Enter state tax withholding rate: "))

#Do calculations for new information needed
gross= hours*payrate
fwithhold= gross*ftax
swithhold= gross*stax
deduction= fwithhold+swithhold
netpay= gross- deduction
ftaxpercent= ftax*100
staxpercent= stax*100

#format the money amounts to have a dollar sign and two decimal places after
#the decimal
payrateInString = str("$")+str(format(payrate, '.2f'))
grossInString = str("$")+str(format(gross, '.2f'))
fwithholdInString = str("$")+str(format(fwithhold, '.2f'))
swithholdInString = str("$")+str(format(swithhold, '.2f'))
deductionInString = str("$")+str(format(deduction, '.2f'))
netpayInString= str("$")+str(format(netpay, '.2f'))

#format the percentages
ftaxInString = str("(")+str(format(ftaxpercent, '.1f'))+str("%):")
staxInString = str("(")+str(format(staxpercent, '.1f'))+str("%):")

#display the payroll statement
print()
print("Employee Name:",name)
print("Hours Worked:", hours)
print("Pay Rate:", payrateInString)
print("Gross Pay:", grossInString)
print("Deductions:")
print("  Federal Withholding",ftaxInString,fwithholdInString)
print("  State Withholding",staxInString, swithholdInString)
print("  Total Deduction:", deductionInString)
print("Net Pay:",netpayInString)


