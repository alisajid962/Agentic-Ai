seat_map = {}
checked_in = set()
boarding_order = []

capacity = int(input("Enter Plane Capacity: "))
no_of_passengers = int(input("Enter Number of Check-ins: "))
for i in range(no_of_passengers):
    passenger = input("Enter Passenger Name: ")
    seat = input("Enter Seat Number: ")
    check = (passenger, seat)

    passenger = check[0]
    seat = check[1]
    if passenger == "NOSHOW":
        print("Passenger did not arrive.")
        continue
    if passenger in checked_in:
        print("Passenger has already checked in.")
        continue
    if seat in seat_map:
        print("Seat is already occupied.")
        continue
    seat_map[seat] = passenger
    checked_in.add(passenger)
    boarding_order.append(passenger)

    print("Check-in Successful.")

    if len(seat_map) == capacity:
        print("Plane is Full.")
        break

print("\nFinal Seat Map")
for i in seat_map:
    print(i, "->", seat_map[i])
print("\nBoarding Order")
for i in boarding_order:
    print(i)

print("\nTotal Passengers Checked In =", len(checked_in))