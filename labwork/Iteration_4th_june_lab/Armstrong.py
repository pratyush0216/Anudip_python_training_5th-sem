# program to check if the number is armstrong or not
#---------------------------------------------------------------
print("---------------Armstrong Number---------------")
# take the number form user
num = int(input("Enter a number: "))
sum = 0
temp = num
# checking the number is armstrong if the sum of the cube of the digit is equal to the number
while temp > 0:
    digit = temp % 10
    sum = sum + digit ** 3
    temp = temp // 10
# the number is armstrong
if sum == num:
    print("Armstrong Number")
# the number is not an armstrong    
else:
    print("Not an Armstrong Number")