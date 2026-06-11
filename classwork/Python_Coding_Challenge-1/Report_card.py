# School Report Card Management System
print("-------- Report Card Management------------")

# Read data from marks.txt
file = open("marks.txt", "r")
data = file.readlines()
file.close()

students = []
topper_name = ""
topper_marks = 0
passed = 0
failed = 0
merit_holders = []

#----------------------------------------
# Process student records
for line in data:
    record = line.strip().split(",")

    sid = record[0]
    name = record[1]
    marks = int(record[2])

    # Grade calculation
    if marks >= 90:
        grade = "A+"
    elif marks >= 80:
        grade = "A"
    elif marks >= 70:
        grade = "B"
    elif marks >= 60:
        grade = "C"
    elif marks >= 40:
        grade = "D"
    else:
        grade = "F"

    # Pass/Fail count
    if marks >= 40:
        passed += 1
    else:
        failed += 1

    # Topper details
    if marks > topper_marks:
        topper_marks = marks
        topper_name = name

    # Merit certificate holders
    if marks >= 90:
        merit_holders.append(name)

    students.append([sid, name, marks, grade])

#------------------------------------------------------
# Generate report_card.txt
report = open("report_card.txt", "w")

for student in students:
    report.write(
        f"ID: {student[0]}, Name: {student[1]}, Marks: {student[2]}, Grade: {student[3]}\n"
    )

report.close()

# Display results
print("Topper:", topper_name, f"({topper_marks})")
print("Passed Students:", passed)
print("Failed Students:", failed)

print("Merit Certificate Holders:")
for name in merit_holders:
    print(name)

print("Report Cards Generated Successfully.")
