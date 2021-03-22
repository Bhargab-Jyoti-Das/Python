#Write a program to prompt the user for hours and rate per hour to compute gross pay
while True:
 hr = input(" Enter hour : ")
 rate = input(" Enter rate : ")
 try:
  hour=float(hr)
  rt=float(rate)
 except:
  print("Please input a number")
  continue
 
 print(" gross pay is ", hour*rt)
 sval = input(' Do you want to continue: ')
 if sval.upper()=="YES": 
   continue
 elif sval.upper()=="NO":
   break 
 else:
   val=input("Please select Yes or NO :")
   if val.upper()=="YES":
    continue
   else:
    break
    
