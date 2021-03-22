 # Pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours
hr = input("Enter no of hours that has been worked: ")
pay = input("Enter pay that needs to be given : ")
try:
	_hr=float(hr)
	_pay=float(pay)
except:
 print("Please enter numeric value!!! ")
 quit()
if _hr>40:
	sal=(_hr * 1.5) * _pay
	print("Overtime  Salary is ", sal)
else:
	print(" Salary is ", (_hr *_pay))
