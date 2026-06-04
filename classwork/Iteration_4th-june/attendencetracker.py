# program to track the attendence of the student either presnt or absent
#--------------------------------------------------------------------
print("---------------Attendence Tracker------------------")
# tracke the present and absent students
present = 0
absent = 0

for i in range(1, 31):
    status = input(f"Student {i} (P for Present / A for Absent): ")

    if status.upper() == "P":
        present += 1
    elif status.upper() == "A":
        absent += 1
    else:
        print("Invalid input! Counted as Absent.")
        absent += 1

print("\nAttendance Report")
print("Total Present Students:", present)
print("Total Absent Students:", absent)