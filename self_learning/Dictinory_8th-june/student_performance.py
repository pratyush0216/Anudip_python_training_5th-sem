# Student Performance Analytics System

students = {
    "S101": {"name": "Anuj", "marks": 85},
    "S102": {"name": "Rahul", "marks": 72},
    "S103": {"name": "Priya", "marks": 91},
    "S104": {"name": "Aman", "marks": 45},
    "S105": {"name": "Neha", "marks": 67},
    "S106": {"name": "Rohan", "marks": 88},
    "S107": {"name": "Karan", "marks": 52},
    "S108": {"name": "Pooja", "marks": 96},
    "S109": {"name": "Vikas", "marks": 39},
    "S110": {"name": "Sneha", "marks": 77},
    "S111": {"name": "Arjun", "marks": 81},
    "S112": {"name": "Meera", "marks": 58},
    "S113": {"name": "Raj", "marks": 93},
    "S114": {"name": "Simran", "marks": 69},
    "S115": {"name": "Deepak", "marks": 48},
    "S116": {"name": "Riya", "marks": 74},
    "S117": {"name": "Mohit", "marks": 87},
    "S118": {"name": "Aditi", "marks": 99},
    "S119": {"name": "Nikhil", "marks": 61},
    "S120": {"name": "Kriti", "marks": 83},
    "S121": {"name": "Sahil", "marks": 55},
    "S122": {"name": "Payal", "marks": 89},
    "S123": {"name": "Yash", "marks": 44},
    "S124": {"name": "Tina", "marks": 78},
    "S125": {"name": "Harsh", "marks": 92},
    "S126": {"name": "Muskan", "marks": 65},
    "S127": {"name": "Akash", "marks": 73},
    "S128": {"name": "Isha", "marks": 86},
    "S129": {"name": "Varun", "marks": 47},
    "S130": {"name": "Naina", "marks": 95}
}

# 1. Display all student records
print("All Student Records:")
for sid, data in students.items():
    print(sid, data)

# 2. Search a student using Student ID
sid = input("\nEnter Student ID to search: ")
if sid in students:
    print("Record Found:", students[sid])
else:
    print("Student not found")

# 3. Add a new student
new_id = input("\nEnter New Student ID: ")
name = input("Enter Name: ")
marks = int(input("Enter Marks: "))
students[new_id] = {"name": name, "marks": marks}
print("Student Added Successfully")

# 4. Update marks of an existing student
update_id = input("\nEnter Student ID to update marks: ")
if update_id in students:
    new_marks = int(input("Enter New Marks: "))
    students[update_id]["marks"] = new_marks
    print("Marks Updated")
else:
    print("Student not found")

# 5. Delete a student
delete_id = input("\nEnter Student ID to delete: ")
if delete_id in students:
    del students[delete_id]
    print("Student Deleted")
else:
    print("Student not found")

# 6. Find topper and lowest scorer
topper = max(students, key=lambda x: students[x]["marks"])
lowest = min(students, key=lambda x: students[x]["marks"])

print("\nTopper:")
print(topper, students[topper])

print("\nLowest Scorer:")
print(lowest, students[lowest])

# 7. Calculate class average
total = 0
for data in students.values():
    total += data["marks"]

average = total / len(students)
print("\nClass Average =", round(average, 2))

# 8. Count pass and fail students
pass_count = 0
fail_count = 0

for data in students.values():
    if data["marks"] >= 50:
        pass_count += 1
    else:
        fail_count += 1

print("\nPass Students =", pass_count)
print("Fail Students =", fail_count)

# 9. Generate Grades
print("\nGrades:")
for sid, data in students.items():
    marks = data["marks"]

    if marks >= 90:
        grade = "A"
    elif marks >= 75:
        grade = "B"
    elif marks >= 50:
        grade = "C"
    else:
        grade = "F"

    print(sid, data["name"], "-", grade)

# 10. Students scoring above average
print("\nStudents Scoring Above Average:")
for sid, data in students.items():
    if data["marks"] > average:
        print(sid, data["name"], data["marks"])

# 11. Top 5 Performers
print("\nTop 5 Performers:")

top5 = sorted(
    students.items(),
    key=lambda x: x[1]["marks"],
    reverse=True
)

for sid, data in top5[:5]:
    print(sid, data["name"], data["marks"])

# 12. Scholarship Students (marks > 85)
scholarship = {}

for sid, data in students.items():
    if data["marks"] > 85:
        scholarship[sid] = data

print("\nScholarship Students:")
for sid, data in scholarship.items():
    print(sid, data)