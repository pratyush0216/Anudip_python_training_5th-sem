#program to check whether three angles form a triangle or not 
print("--------------------triangle angles---------------------------")
#input of three angles
angle1 = int(input("enter first angle (in degree) : "))
#validation of angle1
if (angle1 <= 0):
    exit("angle cannot be zero or negative")
#----------------------------------------------------------------------------
angle2 = int(input("enter second angle (in degree) : "))
#validation of angle2
if (angle2 <= 0):
    exit("angle cannot be zero or negative")
#----------------------------------------------------------------------------
angle3 = int(input("enter third angle (in degree) : "))
#validation of angle3
if (angle3 <= 0):
    exit("angle cannot be zero or negative")
#---------------------------------------------------------------------------
print("---------------------------------------------------")
if (angle1 + angle2 + angle3 == 180):
    print("the angles form a triangle")
else:
    print("the angles do not form a triangle")   
    