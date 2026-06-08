# License Key Verification System
print("------License Verification---------- ")
# # to ask user to enter license key
license_key = input("Enter License Key: ").upper()

# to create list of groups
groups = license_key.split("-")

# to count number of groups
number_of_groups = len(groups)

#------------------------------------------------

# to verify key format
valid = True

if number_of_groups != 4:
    valid = False

for group in groups:
    if len(group) != 4:
        valid = False

#------------------------------------------------

# to remove hyphens and create merged key
merged_key = license_key.replace("-", "")

# to count total letters
total_letters = 0

for ch in merged_key:
    if ch.isalpha():
        total_letters += 1

#------------------------------------------------

# to count vowels
vowels = 0

for ch in merged_key:
    if ch in "AEIOU":
        vowels += 1

#------------------------------------------------

print("-----------------------------------------")
print("License Key:")
print(license_key)

print("\nGroups:")
print(groups)

print("\nNumber of Groups:", number_of_groups)

print("\nTotal Letters:", total_letters)
print("Total Vowels:", vowels)

print("\nMerged Key:")
print(merged_key)

if valid:
    print("\nLicense Key Status: Valid")
else:
    print("\nLicense Key Status: Invalid")