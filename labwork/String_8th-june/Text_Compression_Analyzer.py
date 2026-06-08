#Text Compression Analyzer
print("---------Text Compression---------")
# to ask user to enter text
text = input("Enter Text: ").upper()

#------------------------------------------------

# to create dictionary of character frequencies
frequency = {}

for ch in text:
    if ch in frequency:
        frequency[ch] += 1
    else:
        frequency[ch] = 1

#------------------------------------------------

# to create list of unique characters
unique_characters = list(frequency.keys())

#------------------------------------------------

# to find most frequent character
most_frequent = max(frequency, key=frequency.get)

#------------------------------------------------

# to create compressed output
compressed = ""

count = 1

for i in range(len(text) - 1):
    if text[i] == text[i + 1]:
        count += 1
    else:
        compressed += text[i] + str(count)
        count = 1

compressed += text[-1] + str(count)

#------------------------------------------------

# to calculate compression ratio
original_length = len(text)
compressed_length = len(compressed)

compression_ratio = (compressed_length / original_length) * 100

#------------------------------------------------

print("-----------------------------------------")
print("Original Text:")
print(text)

print("\nCharacter Frequencies:")
for ch in frequency:
    print(ch, "->", frequency[ch])

print("\nUnique Characters:")
print(unique_characters)

print("\nMost Frequent Character:", most_frequent)

print("\nCompressed Output:")
print(compressed)

print("\nOriginal Length:", original_length)
print("Compressed Length:", compressed_length)

print("\nCompression Ratio:", round(compression_ratio, 2), "%")