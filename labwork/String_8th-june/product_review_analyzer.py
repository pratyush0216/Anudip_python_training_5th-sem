# to ask user to enter a review
review = input("Enter Product Review: ").strip()

# to split review into words
words = review.split()

# to count total words
total_words = len(words)

#------------------------------------------------

# to create dictionary containing word frequencies
frequency = {}

for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

#------------------------------------------------

# to find most frequently used word
most_frequent_word = max(frequency, key=frequency.get)

#------------------------------------------------

# to find words appearing only once
once_words = []

for word in frequency:
    if frequency[word] == 1:
        once_words.append(word)

#------------------------------------------------

# to count words having more than 5 characters
count_long_words = 0

for word in words:
    if len(word) > 5:
        count_long_words += 1

#------------------------------------------------

# to display words in reverse order
reverse_words = words[::-1]

#------------------------------------------------

# to create list of unique words
unique_words = list(frequency.keys())

#------------------------------------------------

print("-----------------------------------------")
print("Total Words:", total_words)

print("\nWord Frequencies:")
for word in frequency:
    print(word, "->", frequency[word])

print("\nMost Frequent Word:", most_frequent_word)

print("\nWords Appearing Once:")
print(once_words)

print("\nWords Having More Than 5 Characters:", count_long_words)

print("\nWords In Reverse Order:")
print(reverse_words)

print("\nUnique Words:")
print(unique_words)