# Student Performance Analyzer

marks = [78, 45, 92, 35, 88, 40, 99, 56]

# 1. Display all passed students (marks >= 40)
passed_students = []

# 2. Count failed students
failed_count = 0

# 4. Create a new list containing marks above 75
merit_list = []

# Assume first mark as highest and lowest
highest = marks[0]
lowest = marks[0]

for mark in marks:
    
    # Passed students
    if mark >= 40:
        passed_students.append(mark)
    else:
        failed_count += 1

    # Merit list
    if mark > 75:
        merit_list.append(mark)

    # Find highest mark
    if mark > highest:
        highest = mark

    # Find lowest mark
    if mark < lowest:
        lowest = mark

# Display results
print("Passed Students:", passed_students)
print("Failed Count:", failed_count)
print("Highest Marks:", highest)
print("Lowest Marks:", lowest)
print("Merit List:", merit_list)