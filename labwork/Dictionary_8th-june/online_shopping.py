# Online Shopping Order Analytics

# Make the dictionary of sales with there keys and values 
sales = {
    "Laptop": 15,
    "Mouse": 45,
    "Keyboard": 32,
    "Monitor": 12,
    "Headphones": 28,
    "Printer": 8,
    "Webcam": 20,
    "Speaker": 18,
    "Tablet": 10,
    "Router": 25
}

#-----------------------------------------------------------------------
# Display products sold more than 20 times
print("Products Sold More Than 20 Times:")
for product, qty in sales.items():
    if qty > 20:
        print(product)
#-------------------------------------------------------------------------        
# Find the best-selling product
best_product = max(sales, key=sales.get)
print("\nBest Selling Product:", best_product, "(", sales[best_product], ")", sep="")
#----------------------------------------------------------------------------
# Find the best-selling product
best_product = max(sales, key=sales.get)
print("\nBest Selling Product:", best_product, "(", sales[best_product], ")", sep="")
#-----------------------------------------------------------------------------
# Find the least-selling product
least_product = min(sales, key=sales.get)
print("\nLeast Selling Product:", least_product, "(", sales[least_product], ")", sep="")
#----------------------------------------------------------------------------------
# Calculate total products sold
total_sold = sum(sales.values())
print("\nTotal Units Sold:", total_sold)
#-----------------------------------------------------------------------------------
# Create a list of products requiring promotion (sales < 15)
promotion_products = [product for product, qty in sales.items() if qty < 15]
print("\nProducts Requiring Promotion:")
print(promotion_products)

# Count products having sales between 10 and 30
count = 0
for qty in sales.values():
    if 10 <= qty <= 30:
        count += 1

print("\nProducts Having Sales Between 10 and 30:", count)