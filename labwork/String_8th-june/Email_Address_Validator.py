#Email Address Validator
print("--------Email Address Validator--------")
# # to ask user to enter email
email = input("Enter Email: ").strip()

# to check email is empty or not
if email == "":
    exit("Email cannot be empty.")

#------------------------------------------------

# to extract username
username = email.split("@")[0]

# to extract domain and extension
domain_part = email.split("@")[1]

domain = domain_part.split(".")[0]
extension = domain_part.split(".")[1]

#------------------------------------------------

# to count digits in username
digit_count = 0

for ch in username:
    if ch.isdigit():
        digit_count += 1

#------------------------------------------------

# to count special characters
special_count = 0

for ch in email:
    if not ch.isalnum():
        special_count += 1

#------------------------------------------------

# to validate email
valid = True

# check exactly one @
if email.count("@") != 1:
    valid = False

# check at least one . after @
if "." not in domain_part:
    valid = False

#------------------------------------------------

print("-----------------------------------------")
print("Email:", email)

print("\nUsername:", username)
print("Domain:", domain)
print("Extension:", extension)

print("\nDigits Found:", digit_count)
print("Special Characters Found:", special_count)

if valid:
    print("\nEmail Status: Valid")
else:
    print("\nEmail Status: Invalid")