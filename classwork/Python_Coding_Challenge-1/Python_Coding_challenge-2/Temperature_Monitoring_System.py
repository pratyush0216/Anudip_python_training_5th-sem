#  City Temperature Monitoring System
print("------------Temperature Monitoring System-------------")

# Daily temperatures of different cities
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
#------------------------------------------------

# Cities with temperature above 40°C
above_40 = [city for city, temp in temperature.items() if temp > 40]

#----------------------------------------------------

# Hottest and coolest city
hottest = max(temperature, key=temperature.get)
coolest = min(temperature, key=temperature.get)

#-----------------------------------------------------

# Average temperature
average_temp = sum(temperature.values()) / len(temperature)

#---------------------------------------------------------

# Pleasant cities (<35°C)
pleasant_cities = [city for city, temp in temperature.items() if temp < 35]

# Display results
print("Cities Above 40°C:", above_40)
print("Hottest City:", hottest, f"({temperature[hottest]}°C)")
print("Coolest City:", coolest, f"({temperature[coolest]}°C)")
print("Average Temperature:", round(average_temp, 1), "°C")
print("Pleasant Cities:", pleasant_cities)