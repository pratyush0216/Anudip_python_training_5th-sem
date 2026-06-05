print("----- Prime Number Check -----")

num = int(input("Enter a number: "))

count = 0

if num <= 1:
    print(num, "is not a prime number")

else:
    # Check divisibility up to square root of num
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            count = count + 1
            break

    if count == 0:
        print(num, "is a prime number")
    else:
        print(num, "is not a prime number")

        print("Factors are:")
        for i in range(1, num + 1):
            if num % i == 0:
                print(i)
               


    
       