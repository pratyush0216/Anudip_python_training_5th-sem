# Smart Parking Management System

print("-------Parking mangement---------")
parking_slots = [
    "Occupied", "Vacant", "Occupied", "Vacant", "Occupied",
    "Occupied", "Vacant", "Occupied", "Vacant", "Occupied"
]

# 1. Display vacant parking slot numbers
print("Vacant Parking Slots:", end=" ")
for i in range(len(parking_slots)):
    if parking_slots[i] == "Vacant":
        print(i + 1, end=" ")
print()

# 2. Count occupied and vacant slots
occupied = parking_slots.count("Occupied")
vacant = parking_slots.count("Vacant")

print("Occupied Slots:", occupied)
print("Vacant Slots:", vacant)

# 3. Allocate the first vacant slot
for i in range(len(parking_slots)):
    if parking_slots[i] == "Vacant":
        parking_slots[i] = "Occupied"
        print("Vehicle Allocated to Slot", i + 1)
        break

# 4. Calculate parking occupancy percentage
occupied = parking_slots.count("Occupied")
total_slots = len(parking_slots)

occupancy_percentage = (occupied / total_slots) * 100
print("Occupancy Percentage:", occupancy_percentage, "%")

# 5. Store updated parking information in parking.txt
file = open("parking.txt", "w")

for i in range(len(parking_slots)):
    file.write("Slot " + str(i + 1) + " : " + parking_slots[i] + "\n")

file.close()

print("Parking Details Saved Successfully")