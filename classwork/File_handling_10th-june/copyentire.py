# Open source file in read mode
f1 = open("readme.md", "r")

# Read entire content
content = f1.read()

# Open destination file in write mode
f2 = open("copy.txt", "w")

# Write content into destination file
f2.write(content)

print("File copied successfully.")

# Close both files
f1.close()
f2.close()