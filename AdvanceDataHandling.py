# Initial hotel room structure
hotel_rooms = {
    "101": {"status": "available", "customer": ""},
    "102": {"status": "booked", "customer": "John Doe"}
}

# Function to book a room
def book_room(room_number, customer_name):
    if room_number in hotel_rooms:
        if hotel_rooms[room_number]["status"] == "available":
            hotel_rooms[room_number]["status"] = "booked"
            hotel_rooms[room_number]["customer"] = customer_name
            print(f"Room {room_number} has been booked for {customer_name}.")
        else:
            print(f"Room {room_number} is already booked.")
    else:
        print(f"Room {room_number} does not exist.")

# Function to check-out a customer
def check_out(room_number):
    if room_number in hotel_rooms:
        if hotel_rooms[room_number]["status"] == "booked":
            customer_name = hotel_rooms[room_number]["customer"]
            hotel_rooms[room_number]["status"] = "available"
            hotel_rooms[room_number]["customer"] = ""
            print(f"{customer_name} has checked out of Room {room_number}.")
        else:
            print(f"Room {room_number} is already available.")
    else:
        print(f"Room {room_number} does not exist.")

# Function to display the status of all rooms
def display_rooms_status():
    print("Room Status:")
    for room_number, details in hotel_rooms.items():
        print(f"Room {room_number}: Status - {details['status']}, Customer - {details['customer']}")


print("Initial Room Status:")
display_rooms_status()

print("\nBooking a room:")
book_room("103", "Alice")

print("\nChecking out a customer:")
check_out("102")

print("\nUpdated Room Status:")
display_rooms_status()
