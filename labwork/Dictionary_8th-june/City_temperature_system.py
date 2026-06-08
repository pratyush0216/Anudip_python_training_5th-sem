# City Temperature Monitoring System
# Making the dictionary of states and its temperature
temperature = {
    "Delhi": 41,
    "Mumbai": 33,
    "Chennai": 37,
    "Kolkata": 39,
    "Bengaluru": 28,
    "Pune": 30,
    "Jaipur": 42,
    "Lucknow": 40,
    "Hyderabad": 35,
    "Ahmedabad": 43
}
#-----------------------------------------------------------
# Cities having temperature above 40°C
print("Cities Above 40°C:")
for city, temp in temperature.items():
    if temp > 40:
        print(city)
#-------------------------------------------------------------
# Hottest city
hottest_city = max(temperature, key=temperature.get)
print("\nHottest City:", hottest_city, f"({temperature[hottest_city]}°C)")
#------------------------------------------------------------
# Coolest city
coolest_city = min(temperature, key=temperature.get)
print("Coolest City:", coolest_city, f"({temperature[coolest_city]}°C)")
#-------------------------------------------------------------------
# Average temperature
average_temp = sum(temperature.values()) / len(temperature)
print(f"\nAverage Temperature: {average_temp:.1f}°C")
#-----------------------------------------------------------------------
# Pleasant cities (temperature < 35°C)
pleasant_cities = [city for city, temp in temperature.items() if temp < 35]
print("\nPleasant Cities:")
print(pleasant_cities)
#-----------------------------------------------------------------------
# Count cities with temperature between 35°C and 40°C
count = 0
for temp in temperature.values():
    if 35 <= temp <= 40:
        count += 1

print("\nCities Between 35°C and 40°C:", count)