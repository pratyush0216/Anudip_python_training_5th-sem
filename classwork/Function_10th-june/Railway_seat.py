# railway Reservation seat anlayzer
seats = ["Booked", "Available", "Booked", "Booked", "Available", "Available", "Booked", "Available", "Booked", "Booked", "Available", "Booked" ]
#function to count booked and available seats
def count_seats(seats):
    booked = seats.count("Booked")
    available = seats.count("Available")
    return booked,available
#function to find first available seat
def first_available(seats):
    for i in range(len(seats)):
        if seats[i] == "Available":
            return i + 1                                                   #seat numbers start from 1
#function to calculate occupancy percentage
def occupancy_percentage(seats):
    booked = seats.count("booked")
    total = len(seats)
    return (booked / total) * 100
#function to display available seat numbers
def display_available_seats(seats):
    print("Available seat Number: ",end = " ")
    for i in range(len (seats)):
        if seats[i] == "Available":
            print(i + 1, end = " ")        
#main program
booked,available = count_seats(seats)
print("Booked Seats:", booked)
print("Available seats: ", available)

print("first available sest: ",first_available(seats))

print("Occupancy Percentage: ",round(occupancy_percentage(seats), 2), "%")
display_available_seats(seats)
