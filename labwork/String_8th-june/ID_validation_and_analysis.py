# Employee ID Validation and Analysis System
print("----------------Employee ID Validation and Analysis System----------------")
# Enter the employee ID
emp_id = input("Enter Employee ID: ")

# 1. Count uppercase letters
upper_count = 0

# 2. Count digits
digit_count = 0

# 6. Create list of digits
digit_list = []

# 7. Sum of digits
digit_sum = 0

for ch in emp_id:
    if ch.isupper():
        upper_count += 1

    if ch.isdigit():
        digit_count += 1
        digit_list.append(int(ch))
        digit_sum += int(ch)

# 3. Extract joining year
year = emp_id[3:7]

# 4. Extract employee name
name = emp_id[7:-3]

# 5. Validate ID
valid = True

if not emp_id.startswith("EMP"):
    valid = False

if not year.isdigit() or len(year) != 4:
    valid = False

if not emp_id[-3:].isdigit():
    valid = False

# Display Results
print("\nEmployee ID:", emp_id)

print("\nUppercase Letters:", upper_count)
print("Digits:", digit_count)

print("\nJoining Year:", year)
print("Employee Name:", name)

print("\nDigit List:", digit_list)
print("Sum of Digits:", digit_sum)

if valid:
    print("\nID Status: Valid")
else:
    print("\nID Status: Invalid")