# Ques: write the program to input a sentence and display the frequence of vowel present in the sentence 
# Taking the input from the user
s = input("enter the sentence: ")
a = 0
e = 0
i = 0 
o = 0
u = 0
for ch in s:
    if ch == "a" or ch == "A":
        a += 1
    elif ch == "e" or ch == "E":
        e += 1    
    elif ch == "i" or ch == "I":
        i += 1
    elif ch == "o" or ch == "O":
        o += 1
    elif ch == "u" or ch == "U":
        u += 1

if(a > 0):
    print("a = ",a)
if(e > 0):
    print("e = ",e)
if(i > 0):
    print("i = ",i)
if(o > 0):
    print("o = ",o)
if(u > 0):
    print("u = ",u)
   