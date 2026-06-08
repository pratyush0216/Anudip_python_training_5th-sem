# employee performance Dashboard

# Make the dictionary with the employee id and score
performance = {
    "EMP101": 92,
    "EMP102": 78,
    "EMP103": 45,
    "EMP104": 88,
    "EMP105": 97,
    "EMP106": 56,
    "EMP107": 81,
    "EMP108": 64,
    "EMP109": 39,
    "EMP110": 73
}
#-----------------------------------------------------------------
# Display employees scoring above 80
print("Employees Scoring Above 80:")
for emp, score in performance.items():
    if score > 80:
        print(emp)
#-------------------------------------------------------------------
# Count employees needing improvement (score < 60)
count = 0
for score in performance.values():
    if score < 60:
        count += 1
print("\nEmployees Needing Improvement:", count)
#---------------------------------------------------------------------
# Find the top performer
top_performer = max(performance, key=performance.get)
print("\nTop Performer:", top_performer, "(", performance[top_performer], ")", sep="")
#-----------------------------------------------------------------------
# Calculate average performance score
average_score = sum(performance.values()) / len(performance)
print("\nAverage Score:", round(average_score, 1))
#-----------------------------------------------------------------------
# Create separate lists
excellent = []
good = []
average = []
poor = []

for emp, score in performance.items():
    if score >= 90:
        excellent.append(emp)
    elif 75 <= score <= 89:
        good.append(emp)
    elif 60 <= score <= 74:
        average.append(emp)
    else:
        poor.append(emp)

print("\nExcellent:")
print(excellent)

print("\nGood:")
print(good)

print("\nAverage:")
print(average)

print("\nPoor:")
print(poor)