# Smart Railway Reservation System
print("-------Smart Railway Resvation---------")
# show the status of seats

seats = {
    1: "Booked",
    2: "Available",
    3: "Booked",
    4: "Available",
    5: "Booked",
    6: "Booked",
    7: "Available",
    8: "Booked",
    9: "Available",
    10: "Booked"
}
#----------------------------------------------------------------
# 1.Display all available seat numbers.

print("Available Seats:")
for seat, status in seats.items():
    if status == "Available":
        print(seat, end=" ")

print()

#-------------------------------------------------------------------
#2.Count booked and available seats.

booked = 0
available = 0
for status in seats.values():
    if status == "Booked":
        booked += 1
    else:
        available += 1
print("Booked seats: ",booked)
print("Available seats: ",available)

#------------------------------------------------------------------
#3.Reserve the first available seat.

for seats,staus in seats.items():
    if status == "Available":
        seats[seat] = "Booked"
        print("seat",seat,"reserved succesfully")
        break

#--------------------------------------------------------------
# 4.Cancel booking for a given seat number.

seat_no = int(input("Enter seat number to cancel booking: "))

if seat_no in seats:
    if seats[seat_no] == "Booked":
        seats[seat_no] = "Available"
        print("Booking Cancelled Successfully.")
    else:
        print("Seat is already available.")
else:
    print("Invalid Seat Number.")

#---------------------------------------------------------------------
# 5. Store updated reservation status in reservations.txt
file = open("reservations.txt", "w")

for seat, status in seats.items():
    file.write("Seat " + str(seat) + " : " + status + "\n")

file.close()

print("Reservation Details Saved Successfully.")

#----------------------------------------------------------------------
# 6. Display occupancy percentage
booked = 0

for status in seats.values():
    if status == "Booked":
        booked += 1

occupancy = (booked / len(seats)) * 100

print("Occupancy Percentage:", occupancy, "%")