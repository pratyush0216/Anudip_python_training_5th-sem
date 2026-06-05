# Number Guessing Game using Iteration

print("----- Number Guessing Game -----")

# Secret number
secret_number = 25

# Counter for attempts
attempts = 0

# Loop until correct guess
while True:
    
    guess = int(input("Enter your guess: "))
    
    attempts += 1
    
    if guess > secret_number:
        print("Too High")
    
    elif guess < secret_number:
        print("Too Low")
    
    else:
        print("Correct Guess")
        print("Total Attempts =", attempts)
        break