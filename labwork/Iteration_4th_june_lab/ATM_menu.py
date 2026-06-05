# ATM Simulation System

# Initial balance
balance = 10000

while True:
    
    print("\n----- ATM MENU -----")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    
    choice = int(input("Enter your choice: "))
    
    # Check Balance
    if choice == 1:
        print("Current Balance = ₹", balance)
    
    # Deposit Money
    elif choice == 2:
        amount = float(input("Enter deposit amount: ₹"))
        balance = balance + amount
        print("Amount Deposited Successfully")
        print("Updated Balance = ₹", balance)
    
    # Withdraw Money
    elif choice == 3:
        amount = float(input("Enter withdrawal amount: ₹"))
        
        if amount <= balance:
            balance = balance - amount
            print("Withdrawal Successful")
            print("Remaining Balance = ₹", balance)
        else:
            print("Insufficient Balance")
    
    # Exit
    elif choice == 4:
        print("Thank You for Using ATM")
        break
    
    # Invalid Choice
    else:
        print("Invalid Choice! Please try again.")