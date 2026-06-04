# program to show the electricity used and its lies in  which  categiores
# Input units consumed
print("-----------Electricity-----------------")
# Enter the unit consumed by the user
units = int(input("Enter electricity units consumed: "))
# Calculate bill based on slab rates
# Determine consumption category
if units <= 100:
    bill = units * 5
    category = "Low Consumption"
elif units <= 200:
    bill = (100 * 5) + ((units - 100) * 7)
    category = "Medium Consumption"
else:
    bill = (100 * 5) + (100 * 7) + ((units - 200) * 10)
    category = "High Consumption"

# Display results
print("\nElectricity Bill Details")
print("Units Consumed :", units)
print("Total Bill     : ₹", bill)
print("Category       :", category)