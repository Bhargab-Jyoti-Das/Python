# Rewriting Pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours with the help of function
# Getting input from user
hr = input("Enter no of hours that has been worked: ")
pay = input("Enter pay that needs to be given : ")

# Use of try and except incase user enter wrong type value
try:
	_hr=float(hr)
	_pay=float(pay)
except:
 print("Please enter numeric value!!! ")
 quit()

def computepay(hours, rate): # defining a function compute to invole when called 
 if hours>40:
    sal=(hours * 1.5) * rate
    #print("Overtime  Salary is ",sal)
 else:
    sal=hours * rate
    #print(" Salary is ",sal)
 return sal

z=computepay(_hr,_pay)
print("Salary is :", z)
