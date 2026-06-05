# ATM Transaction History

transactions = [5000, -2000, 3000, -1000, -500, 7000]

balance = 0
deposits = []
withdrawals = []

# Assume first deposit and withdrawal as largest
largest_deposit = 0
largest_withdrawal = transactions[1]  # -2000

for amount in transactions:

    # Calculate current balance
    balance += amount

    # Separate deposits and withdrawals
    if amount > 0:
        deposits.append(amount)

        # Find largest deposit
        if amount > largest_deposit:
            largest_deposit = amount

    else:
        withdrawals.append(amount)

        # Find largest withdrawal (most negative value)
        if amount < largest_withdrawal:
            largest_withdrawal = amount

# Display results
print("Current Balance:", balance)
print("Deposits:", deposits)
print("Withdrawals:", withdrawals)
print("Total Deposits:", len(deposits))
print("Total Withdrawals:", len(withdrawals))
print("Largest Deposit:", largest_deposit)
print("Largest Withdrawal:", largest_withdrawal)