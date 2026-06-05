# Palindrome and Reverse Number Checker
#----------------------------------------------------------------------
# Take input from user
print("----------------palindrome--------------")
num = int(input("Enter a number: "))

# Store original number
original = num

# Variable to store reverse number
reverse = 0

# Reverse the number using iteration
while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

# Display reverse number
print("Reverse:", reverse)

# Check palindrome
if original == reverse:
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")