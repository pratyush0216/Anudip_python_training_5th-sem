# Program to check the number is a strong number 
#-------------------------------------------------
print("---------Strong factorial--------------")
# taking input form user
num = int(input("Enter a number: "))

temp = num
sum = 0
# the  Strong Number is a number whose sum of factorials of digits equals the number itself
while temp > 0:
    digit = temp % 10
    fact = 1
    for i in range(1, digit + 1):
        fact = fact * i
# factorial is adding         
    sum = sum + fact
    temp = temp // 10

if sum == num:
    print("Strong Number")
#------------------------------------------------------------------    
else:
    print("Not a Strong Number")