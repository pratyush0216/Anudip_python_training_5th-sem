# Inventory Stock Alert System

stock = [25, 5, 0, 12, 3, 18, 0, 30]

# 1. Count products that are out of stock
out_of_stock = stock.count(0)

# 2. Products that need restocking (quantity less than 10)
restock_required = []
for item in stock:
    if item < 10:
        restock_required.append(item)

# 3. Count available products (stock greater than 0)
available_products = 0
for item in stock:
    if item > 0:
        available_products += 1

# 4. Products with healthy stock (greater than or equal to 15)
healthy_stock = []
for item in stock:
    if item >= 15:
        healthy_stock.append(item)

# Display Results
print("Out of Stock Products:", out_of_stock)
print("Restock Required:", restock_required)
print("Available Products:", available_products)
print("Healthy Stock:", healthy_stock)