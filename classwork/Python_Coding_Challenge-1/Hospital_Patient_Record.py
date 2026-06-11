# Hospital patient Record management system
# Create sample patients.txt file first with the given data

# Function to display all patient recoard
def display_records():
    file = open("patients.txt","r")
    print("All Patient records: ")
    for line in file:
        print(Line.strip())
    file.close()

#-------------------------------------------------------------
# # Function to display critical patients
def critical_patients():
    file = open("patients.txt", "r")
    print("\nCritical Patients:")
    for line in file:
        data = line.strip().split(",")
        if data[2] == "Critical":
            print(data[1])
    file.close()

#------------------------------------------------------------------
# Function to count patients under each status
def count_patients():
    normal = 0
    stable = 0
    critical = 0

    file = open("patients.txt", "r")
    for line in file:
        data = line.strip().split(",")
        if data[2] == "Normal":
            normal += 1
        elif data[2] == "Stable":
            stable += 1
        elif data[2] == "Critical":
            critical += 1
    file.close()

    print("\nPatient Count:")
    print("Normal :", normal)
    print("Stable :", stable)
    print("Critical :", critical)

#--------------------------------------------------------------------
# Function to search patient by ID
def search_patient(pid):
    file = open("patients.txt", "r")
    found = False

    for line in file:
        data = line.strip()
        if data.startswith(pid):
            print("\nPatient Found:")
            print(data)
            found = True
            break

    if not found:
        print("\nPatient Not Found")

    file.close()

#---------------------------------------------------------------------------------
# Function to save critical patients
def save_critical():
    file = open("patients.txt", "r")
    critical_file = open("critical_patients.txt", "w")

    for line in file:
        data = line.strip().split(",")
        if data[2] == "Critical":
            critical_file.write(line)

    file.close()
    critical_file.close()

    print("\nCritical Patient Report Generated Successfully.")

#------------------------------------------------------------------------------------
# Main Program
display_records()
critical_patients()
count_patients()

pid = input("\nEnter Patient ID to Search: ")
search_patient(pid)

save_critical()