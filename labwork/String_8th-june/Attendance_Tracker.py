#String-Based Attendance Tracker
print("------String-Based Attendance Tracker---------")
# to ask user to enter attendance record
attendance = input("Enter Attendance Record: ").upper()

# to count present and absent days
present_days = attendance.count("P")
absent_days = attendance.count("A")

# to calculate attendance percentage
total_days = len(attendance)
attendance_percentage = (present_days / total_days) * 100

#------------------------------------------------

# to find longest present streak
current_present = 0
longest_present = 0

for ch in attendance:
    if ch == "P":
        current_present += 1
        if current_present > longest_present:
            longest_present = current_present
    else:
        current_present = 0

#------------------------------------------------

# to find longest absent streak
current_absent = 0
longest_absent = 0

for ch in attendance:
    if ch == "A":
        current_absent += 1
        if current_absent > longest_absent:
            longest_absent = current_absent
    else:
        current_absent = 0

#------------------------------------------------

# to determine attendance status
if attendance_percentage < 75:
    status = "Below 75%"
else:
    status = "Above 75%"

#------------------------------------------------

print("-----------------------------------------")
print("Attendance Record:")
print(attendance)

print("\nPresent Days:", present_days)
print("Absent Days:", absent_days)

print("\nAttendance Percentage:", round(attendance_percentage, 2), "%")

print("\nLongest Present Streak:", longest_present)
print("Longest Absent Streak:", longest_absent)

print("\nAttendance Status:", status)