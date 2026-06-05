# Mini Employee Payroll System

# Accept employee details
name = input("Enter Employee Name: ")
basic_salary = float(input("Enter Basic Salary: ₹"))

# Calculate salary components
hra = basic_salary * 20 / 100
da = basic_salary * 10 / 100
pf = basic_salary * 12 / 100

# Calculate Gross and Net Salary
gross_salary = basic_salary + hra + da
net_salary = gross_salary - pf

# Display details
print("\n----- Employee Payroll Details -----")
print("Employee Name :", name)
print("Basic Salary  : ₹", basic_salary)
print("HRA (20%)     : ₹", hra)
print("DA (10%)      : ₹", da)
print("PF (12%)      : ₹", pf)
print("Gross Salary  : ₹", gross_salary)
print("Net Salary    : ₹", net_salary)

# Determine Grade
if net_salary > 50000:
    print("Grade : Senior Grade")
elif net_salary > 30000:
    print("Grade : Mid Grade")
else:
    print("Grade : Junior Grade")