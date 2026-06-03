#calculating simple interest(validation)
print("------------simple interest-----------------")
p = float(input("enter the principal amount : "))
r = float(input("enter the rate of interest(in %) : "))
t = int(input("enter the time (in year) : "))
#--------------------------------------------
if p>0 and r>0 and t>0:
#calculation S.I
   si = (p * r * t)/100
   print("the simple interest is : ", si)
else:
    print("invalid input. please enter positive values for principal, rate and time.")


