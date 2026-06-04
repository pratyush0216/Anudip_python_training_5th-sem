# Program to check the number is prime or not 
print("----------------Prime Number----------------")
#  Taking a number form user 
num = int(input("Enter a number: "))
# checking the number is prime or not 
if num > 1:
    for i in range(2, num):  
        if(num % i) == 0:
            print(num, "is not a prime number ")
            break
        if num == 2:
            print(num, "is a prime number ")
            break
        else:
            print(num, "is a prime number ")
    2  
#------------------------------------------------------------
# The Factor of the number 
print("The factors of the number are: ")
for i in range(1, num + 1):
    if(num % i) == 0:
        print(i)
               


    
       