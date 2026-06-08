# Ques: write a program to input a string and input a sentence from user and count the number of character present in it without using len function
#Taking the input from the user 
s = input("enter the sentence: ")
count = 0
for ch in s:
    if ch in s:
        count += 1
print("charcter are:",count)
