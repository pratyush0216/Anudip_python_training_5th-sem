# Food Delivery Performance Tracker

delivery_time = [28, 45, 60, 22, 35, 80, 40, 25, 55, 18]

# Function to find fastest delivery
def fastest_delivery(times):
    return min(times)

# Function to find delayed orders
def delayed_orders(times):
    delayed = []

    for time in times:
        if time > 45:
            delayed.append(time)

    return delayed

# Function to calculate average delivery time
def average_delivery_time(times):
    total = 0

    for time in times:
        total += time

    avg = total / len(times)
    return avg

# Function to display categories
def delivery_category(times):
    print("Categories:")

    for time in times:
        if time <= 30:
            print(time, "-> Fast")
        elif time <= 45:
            print(time, "-> Normal")
        else:
            print(time, "-> Delayed")


# Main Program

print("Fastest Delivery:", fastest_delivery(delivery_time), "minutes")

print("Delayed Orders:", delayed_orders(delivery_time))

print("Average Delivery Time:", round(average_delivery_time(delivery_time), 1), "minutes")

delivery_category(delivery_time)