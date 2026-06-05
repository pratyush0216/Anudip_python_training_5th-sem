# Program to verfy the correct ATM pin 
print("---------------ATM Pin Verification------------------")
correct_pin = 1234
# User enter the pin
while True:
    pin = int(input("Enter your PIN: "))

    if pin == correct_pin:
        print("Access Granted!")
        break
# The pin is incorrect then    
    else:
        print("Incorrect PIN. Try Again.")