# Program to draw number pymird pattern
# Accept number of rows from the user
#----------------------------------------------------
print("-----------pyramid pattern------------")
rows = int(input("Enter number of rows: "))

# Print the increasing pattern
print("Increasing Pattern:")
for i in range(1, rows + 1):      # Controls rows
    for j in range(1, i + 1):     # Prints numbers from 1 to i
        print(j, end="")
    print()                       # Move to next line
#-------------------------------------------------------------------
# Print the reverse pattern
print("\nReverse Pattern:")
for i in range(rows, 0, -1):      # Starts from rows and decreases to 1
    for j in range(1, i + 1):     # Prints numbers from 1 to i
        print(j, end="")
    print()                       # Move to next line