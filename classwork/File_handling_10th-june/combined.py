#To read the data from file and display the following:
#1. No. of Vowels in file.
#2. No. of characters into the file.
#3. No. of lines into the file.

#open the file in read mode
file = open("data.txt", "r")

#read all contents of the file 
content = file.read()

#count vowels
vowels = 0
for ch in content:
    if ch.lower() in "aeiouAEIOU":
        vowels += 1
 
#count characters 
characters = len(content)

#count lines
file.seek(0)                                      #Move cursor back to beginninig
lines = len(file.readlines())

#Display results
print("Number of vowels : ", vowels)
print("Number of characters : ", characters)
print("Number of lines : ", lines)

#close the file
file.close
