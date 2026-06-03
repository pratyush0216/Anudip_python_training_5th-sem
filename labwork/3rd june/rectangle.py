#program to calculate the area and parameter of rectangle(validation included)
#----------------------------------------------------------------------
print("------------RECTANGLE-----------------")
#taking input from user
l = int(input("enter the length of rectangle(in cm) : "))
b = int(input("enter the breadth of rectangle(in cm) : "))
#-----------------------------------------------------
#calculation area 
if l>0 and b>0:
   area = l * b
   print("the area of rectangle is : ", area, "sq.cm")
#-------------------------------------------------------
#Ccalculate perimeter
   perimeter = 2 * (l + b)
   print("the perimeter of rectangle is : ", perimeter, "cm")
else:
     print("invalid input. please enter positive values for length and breadth.")

