library = {
"B101":{"title":"Python Basics","author":"ABC","copies":5},
"B102":{"title":"C Programming","author":"XYZ","copies":2},
"B103":{"title":"Java Fundamentals","author":"PQR","copies":7},
"B104":{"title":"Data Structures","author":"LMN","copies":1},
"B105":{"title":"DBMS","author":"RST","copies":0},
"B106":{"title":"Operating System","author":"JKL","copies":4},
"B107":{"title":"Computer Networks","author":"DEF","copies":2},
"B108":{"title":"AI Basics","author":"GHI","copies":6},
"B109":{"title":"Machine Learning","author":"MNO","copies":3},
"B110":{"title":"Cyber Security","author":"UVW","copies":0},
"B111":{"title":"Cloud Computing","author":"AAA","copies":5},
"B112":{"title":"Software Engineering","author":"BBB","copies":2},
"B113":{"title":"Big Data","author":"CCC","copies":8},
"B114":{"title":"Data Mining","author":"DDD","copies":1},
"B115":{"title":"Web Development","author":"EEE","copies":4},
"B116":{"title":"HTML Guide","author":"FFF","copies":7},
"B117":{"title":"CSS Master","author":"GGG","copies":2},
"B118":{"title":"JavaScript","author":"HHH","copies":6},
"B119":{"title":"PHP Basics","author":"III","copies":1},
"B120":{"title":"Linux","author":"JJJ","copies":0},
"B121":{"title":"Unix","author":"KKK","copies":3},
"B122":{"title":"Android Dev","author":"LLL","copies":5},
"B123":{"title":"Python Advanced","author":"MMM","copies":9},
"B124":{"title":"React JS","author":"NNN","copies":2},
"B125":{"title":"Node JS","author":"OOO","copies":4},
"B126":{"title":"Django","author":"PPP","copies":1},
"B127":{"title":"Flask","author":"QQQ","copies":5},
"B128":{"title":"DevOps","author":"RRR","copies":2},
"B129":{"title":"Blockchain","author":"SSS","copies":1},
"B130":{"title":"IoT","author":"TTT","copies":6}
}

# 1. Add Book
bid = input("Enter Book ID : ")
title = input("Enter Title : ")
author = input("Enter Author : ")
copies = int(input("Enter Copies : "))

library[bid] = {
    "title": title,
    "author": author,
    "copies": copies
}

# 2. Remove Book
bid = input("\nEnter Book ID to Remove : ")

if bid in library:
    del library[bid]

# 3. Search by ID
bid = input("\nEnter Book ID to Search : ")

if bid in library:
    print(library[bid])
else:
    print("Book Not Found")

# 4. Search by Title
title = input("\nEnter Title : ")

for bid in library:
    if library[bid]["title"] == title:
        print(bid, library[bid])

# 5. Update Copies
bid = input("\nEnter Book ID : ")

if bid in library:
    copies = int(input("Enter New Copies : "))
    library[bid]["copies"] = copies

# 6. Issue Book
bid = input("\nEnter Book ID to Issue : ")

if bid in library:
    if library[bid]["copies"] > 0:
        library[bid]["copies"] = library[bid]["copies"] - 1
        print("Book Issued")
    else:
        print("Book Not Available")

# 7. Return Book
bid = input("\nEnter Book ID to Return : ")

if bid in library:
    library[bid]["copies"] = library[bid]["copies"] + 1
    print("Book Returned")

# Variables for Reports
purchase = {}

first = True
total_books = 0

for bid in library:

    copies = library[bid]["copies"]

    total_books = total_books + copies

    if first:
        maxcopies = copies
        most = bid
        first = False

    if copies > maxcopies:
        maxcopies = copies
        most = bid

    if copies < 3:
        purchase[bid] = library[bid]

# 8. Books with fewer than 3 copies
print("\nBOOKS WITH LESS THAN 3 COPIES")

for bid in library:
    if library[bid]["copies"] < 3:
        print(bid, library[bid])

# 9. Unavailable Books
print("\nUNAVAILABLE BOOKS")

for bid in library:
    if library[bid]["copies"] == 0:
        print(bid, library[bid])

# 10. Most Available Book
print("\nMOST AVAILABLE BOOK")
print(most, library[most])

# 11. Restocking Report
print("\nRESTOCKING REPORT")

for bid in library:
    if library[bid]["copies"] < 3:
        print(bid, library[bid]["title"], library[bid]["copies"])

# 12. Books Requiring Immediate Purchase
print("\nIMMEDIATE PURCHASE BOOKS")

for bid in purchase:
    print(bid, purchase[bid])

# Library Summary Report
print("\n===== LIBRARY SUMMARY REPORT =====")

print("Total Titles =", len(library))
print("Total Available Copies =", total_books)
print("Most Available Book =", library[most]["title"])
print("Books Requiring Purchase =", len(purchase))

out = 0

for bid in library:
    if library[bid]["copies"] == 0:
        out = out + 1

print("Unavailable Books =", out)