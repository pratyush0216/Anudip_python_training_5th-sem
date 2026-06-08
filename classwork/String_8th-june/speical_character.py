# Ques: write a program to input a sentence from user and count the number of speical characters present in the sentence.
# Taking the input from the user
 
sentence = input("Enter a sentence : ")
count = 0
for ch in sentence:
    if ch in "!~@#$%^&*?":
        count += 1
print("specical char:",count)