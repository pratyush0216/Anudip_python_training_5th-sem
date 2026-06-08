# Password Strength Analyzer
# Create the password 
password = input("Enter Password: ")

upper = 0
lower = 0
digit = 0
special = 0

digits_found = []
special_found = []

for ch in password:
    if ch.isupper():
        upper += 1

    elif ch.islower():
        lower += 1

    elif ch.isdigit():
        digit += 1
        digits_found.append(ch)

    else:
        special += 1
        special_found.append(ch)

print("\nPassword:", password)
# Password: Python@2026!

print("\nUppercase Letters:", upper)
# Uppercase Letters: 1

print("Lowercase Letters:", lower)
# Lowercase Letters: 5

print("Digits:", digit)
# Digits: 4

print("Special Characters:", special)
# Special Characters: 2

print("\nDigits Found:", digits_found)
# Digits Found: ['2', '0', '2', '6']

print("Special Characters Found:", special_found)
# Special Characters Found: ['@', '!']

# Checking Password Strength
if len(password) >= 8 and upper >= 1 and lower >= 1 and digit >= 1 and special >= 1:
    strength = "Strong"
elif len(password) >= 6 and (upper > 0 or lower > 0) and digit > 0:
    strength = "Medium"
else:
    strength = "Weak"

print("\nPassword Strength:", strength)
