# Smart Electricity Billing System
# makind the dictionary of house no. and units use by the house
units = {
    "House101": 320,
    "House102": 180,
    "House103": 510,
    "House104": 275,
    "House105": 150,
    "House106": 430,
    "House107": 220,
    "House108": 390,
    "House109": 145,
    "House110": 600
}
#-----------------------------------------------------------
# Houses consuming more than 400 units
print("Houses Consuming More Than 400 Units:")
for house, unit in units.items():
    if unit > 400:
        print(house)
#------------------------------------------------------------
# Highest-consuming house
highest_house = max(units, key=units.get)
print("\nHighest Consumption:")
print(f"{highest_house} ({units[highest_house]} units)")
#----------------------------------------------------------
# Lowest-consuming house
lowest_house = min(units, key=units.get)
print("\nLowest Consumption:")
print(f"{lowest_house} ({units[lowest_house]} units)")
#-----------------------------------------------------------
# Total units consumed
total_units = sum(units.values())
print("\nTotal Units Consumed:", total_units)
#------------------------------------------------------------
# Create lists
low_consumption = []
medium_consumption = []
high_consumption = []

for house, unit in units.items():
    if unit < 200:
        low_consumption.append(house)
    elif 200 <= unit <= 400:
        medium_consumption.append(house)
    else:
        high_consumption.append(house)

print("\nLow Consumption:")
print(low_consumption)

print("\nMedium Consumption:")
print(medium_consumption)

print("\nHigh Consumption:")
print(high_consumption)
#----------------------------------------------------------
# Houses eligible for energy-saving campaign
eligible_count = 0
for unit in units.values():
    if unit > 300:
        eligible_count += 1

print("\nEligible for Energy-Saving Campaign:", eligible_count)