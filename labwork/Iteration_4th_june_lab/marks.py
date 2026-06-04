# program to make Student Result Management System 
#----------------------------------------------------
print("-------------Student Result-------------")
total = 0
# Take the input of 5 subject
for i in range(1, 6):
    marks = float(input(f"Enter marks of Subject {i}: "))
    total += marks
# calculate the percentage
# --------------------------------------------
percentage = total / 5
# print the total marks
print("Total Marks =", total)
# print the percentage
print("Percentage =", percentage)
#-------------------------------------------------
# giving grade according to there mark 
if percentage >= 90:
    print("Grade = A+")
elif percentage >= 75:
    print("Grade = A")
elif percentage >= 60:
    print("Grade = B")
elif percentage >= 40:
    print("Grade = C")
else:
    print("Grade = Fail")