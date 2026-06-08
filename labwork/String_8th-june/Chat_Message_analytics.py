# Chat Message Analytics
print("---------Chat Message Analytics----------")
# # to ask user to enter a message
message = input("Enter Message: ").strip()

# to count total characters
total_characters = len(message)

# to split message into words
words = message.split()

# to count total words
total_words = len(words)

# to find longest word
longest_word = max(words, key=len)

# to find shortest word
shortest_word = min(words, key=len)

# to count occurrences of Python
python_count = words.count("Python")

# to create list of words having more than 4 characters
long_words = []

for word in words:
    if len(word) > 4:
        long_words.append(word)

# to create list of words starting with a vowel
vowel_words = []

for word in words:
    if word[0].lower() in "aeiou":
        vowel_words.append(word)

# to count vowels and consonants
vowels = 0
consonants = 0

for ch in message:
    if ch.isalpha():
        if ch.lower() in "aeiou":
            vowels += 1
        else:
            consonants += 1

#------------------------------------------------

print("-----------------------------------------")
print("Message:")
print(message)

print("\nTotal Characters:", total_characters)
print("Total Words:", total_words)

print("\nLongest Word:", longest_word)
print("Shortest Word:", shortest_word)

print("\nOccurrences of Python:", python_count)

print("\nWords Longer Than 4 Characters:")
print(long_words)

print("\nWords Starting With a Vowel:")
print(vowel_words)

print("\nVowels:", vowels)
print("Consonants:", consonants)