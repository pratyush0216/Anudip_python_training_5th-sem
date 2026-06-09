# E-Commerce Inventory & Sales Dashboard

products = {
"P101":{"name":"Laptop","price":55000,"stock":12,"sold":25},
"P102":{"name":"Mouse","price":800,"stock":20,"sold":40},
"P103":{"name":"Keyboard","price":1500,"stock":15,"sold":18},
"P104":{"name":"Monitor","price":12000,"stock":4,"sold":12},
"P105":{"name":"Printer","price":7000,"stock":0,"sold":8},
"P106":{"name":"Speaker","price":2500,"stock":10,"sold":15},
"P107":{"name":"Webcam","price":1800,"stock":3,"sold":6},
"P108":{"name":"SSD","price":4500,"stock":8,"sold":22},
"P109":{"name":"Hard Disk","price":3500,"stock":2,"sold":9},
"P110":{"name":"Pendrive","price":600,"stock":30,"sold":50},
"P111":{"name":"Router","price":2200,"stock":5,"sold":14},
"P112":{"name":"Projector","price":25000,"stock":2,"sold":4},
"P113":{"name":"Tablet","price":18000,"stock":7,"sold":11},
"P114":{"name":"Phone","price":30000,"stock":9,"sold":35},
"P115":{"name":"Charger","price":900,"stock":25,"sold":45},
"P116":{"name":"Headphone","price":2000,"stock":6,"sold":20},
"P117":{"name":"Smartwatch","price":5000,"stock":4,"sold":13},
"P118":{"name":"Camera","price":45000,"stock":1,"sold":3},
"P119":{"name":"Microphone","price":3000,"stock":5,"sold":7},
"P120":{"name":"Scanner","price":6500,"stock":0,"sold":5},
"P121":{"name":"UPS","price":4000,"stock":8,"sold":16},
"P122":{"name":"Graphics Card","price":35000,"stock":3,"sold":10},
"P123":{"name":"RAM","price":2800,"stock":12,"sold":24},
"P124":{"name":"Motherboard","price":9000,"stock":4,"sold":8},
"P125":{"name":"Processor","price":15000,"stock":6,"sold":17},
"P126":{"name":"Cooling Fan","price":1200,"stock":10,"sold":9},
"P127":{"name":"Power Bank","price":1800,"stock":7,"sold":21},
"P128":{"name":"HDMI Cable","price":500,"stock":18,"sold":30},
"P129":{"name":"LAN Cable","price":300,"stock":2,"sold":11},
"P130":{"name":"Bluetooth Adapter","price":700,"stock":4,"sold":6}
}

# 1. Display all products
print("ALL PRODUCTS")
for pid in products:
    print(pid, products[pid])

# 2. Add new product
pid = input("\nEnter New Product ID : ")
name = input("Enter Product Name : ")
price = int(input("Enter Price : "))
stock = int(input("Enter Stock : "))
sold = int(input("Enter Sold Quantity : "))

products[pid] = {
    "name": name,
    "price": price,
    "stock": stock,
    "sold": sold
}

# 3. Update stock after sales
pid = input("\nEnter Product ID for Sale : ")

if pid in products:
    qty = int(input("Enter Quantity Sold : "))
    products[pid]["stock"] = products[pid]["stock"] - qty
    products[pid]["sold"] = products[pid]["sold"] + qty

# 4,5,6,7,8,9,10,11,12
inventory_value = 0
revenue = 0
total_sales = 0
count = 0

promotion = {}

first = True

for pid in products:

    stock = products[pid]["stock"]
    sold = products[pid]["sold"]
    price = products[pid]["price"]

    inventory_value = inventory_value + (price * stock)
    revenue = revenue + (price * sold)

    total_sales = total_sales + sold
    count = count + 1

    if first:
        best = pid
        least = pid
        maxsale = sold
        minsale = sold
        first = False

    if sold > maxsale:
        maxsale = sold
        best = pid

    if sold < minsale:
        minsale = sold
        least = pid

    if sold < 10:
        promotion[pid] = products[pid]

average_sales = total_sales / count

print("\nOUT OF STOCK PRODUCTS")
for pid in products:
    if products[pid]["stock"] == 0:
        print(pid, products[pid]["name"])

print("\nLOW STOCK PRODUCTS")
for pid in products:
    if products[pid]["stock"] < 5:
        print(pid, products[pid]["name"], products[pid]["stock"])

print("\nTOTAL INVENTORY VALUE =", inventory_value)

print("\nBEST SELLING PRODUCT")
print(best, products[best])

print("\nLEAST SELLING PRODUCT")
print(least, products[least])

print("\nTOTAL REVENUE =", revenue)

print("\nLOW STOCK REPORT")
for pid in products:
    if products[pid]["stock"] < 5:
        print(pid, products[pid]["name"], products[pid]["stock"])

print("\nPRODUCTS WITH SALES ABOVE AVERAGE")
for pid in products:
    if products[pid]["sold"] > average_sales:
        print(pid, products[pid]["name"], products[pid]["sold"])

print("\nPROMOTION PRODUCTS (Sales < 10)")
for pid in promotion:
    print(pid, promotion[pid])

print("\n===== BUSINESS REPORT =====")
print("Total Products =", count)
print("Inventory Value =", inventory_value)
print("Total Revenue =", revenue)
print("Average Sales =", average_sales)
print("Best Selling Product =", products[best]["name"])
print("Least Selling Product =", products[least]["name"])
print("Promotion Products =", len(promotion))