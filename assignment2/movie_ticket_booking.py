available_seats = [
    
    ("A", 1), ("A", 2), ("A", 3),

]
capacity = len(available_seats)
booked_seats = set()
seat_customer = {}
confirmed_bookings = []
while True:
    if len(booked_seats) == capacity:
        print("\nHall is Full")
     
        break
    name = input("\nEnter Customer Name: ")
    row = input("Enter Row (A/B): ").upper()
    number = int(input("Enter Seat Number: "))
    seat = (row, number)
    if seat not in available_seats:
        print("Invalid Seat")
        continue
    if seat in booked_seats:
        print("Seat Already Booked")
    else:
        booked_seats.add(seat)
        seat_customer[seat] = name
        confirmed_bookings.append((name, seat))
        print("Booking Confirmed")
for seat, customer in seat_customer.items():
    print(seat, "->", customer)
print("\nTotal Seats Sold:", len(booked_seats))