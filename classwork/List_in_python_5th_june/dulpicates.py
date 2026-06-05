# A program to create a list of 20 number by the user ask the user to input any other number.Remove all the duplicate enter of this number inform the list
#-----------------------------------------------------------------------------------
print("------Create a list-------")

number = []
# Taking the input for user
for x in range(20):
    num = int(input("Enter a number : "))
# append into list
    number.append(num)
    print("----------------------------------------")
    element = int(input("Enetr any number to remove its duplicate  : ")) 
# Finding the frequency of give number
frequency = number.count(element)
if frequence == 1:
    print("element not found ")
elif frequency == 0 :
    print(" no duplicates found")
else:
    # Reversing the list
    number.reverse()
    for i in range(1, frequency):
        nnumber.remove(element)
# reversing the list agian
    number.reverse()
    print("after remove duplicates")
    print(number)
