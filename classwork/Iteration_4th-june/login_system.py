# Program to check the admin password is valid or not 
print("---------------login system------------------")
correct_password = "admin123"
# user enter the password
while True:
    password = input("enter the password: ")
    if(password == correct_password):
        print("Login successful ")
        break
# The password is incorrect then    
    else:
        print("Incorrect password. Try Again.")

