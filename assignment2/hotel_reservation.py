available_rooms = {"D1", "D2", "S1", "S2", "E1", "E2"}
room_guest = {}
confirmed_guests = []
total_revenue = 0
no_of_reservations = int(input("Enter Number of Reservations: "))
for i in range(no_of_reservations):
    guest = input("Enter Guest Name: ")
    room_type = input("Enter Room Type (Deluxe/Standard/Economy): ")
    reservation = (guest, room_type)
    guest = reservation[0]
    room_type = reservation[1]

    room_number = ""
    if room_type == "Deluxe":
        price = 10000
        if "D1" in available_rooms:
            room_number = "D1"
        elif "D2" in available_rooms:
            room_number = "D2"
        else:
            print("No Deluxe Room Available.")
            continue
    elif room_type == "Standard":

        price = 7000

        if "S1" in available_rooms:
            room_number = "S1"

        elif "S2" in available_rooms:
            room_number = "S2"

        else:
            print("No Standard Room Available.")
            continue

    elif room_type == "Economy":

        price = 5000

        if "E1" in available_rooms:
            room_number = "E1"

        elif "E2" in available_rooms:
            room_number = "E2"

        else:
            print("No Economy Room Available.")
            continue

    else:
        print("Invalid Room Type.")
        continue

    available_rooms.remove(room_number)
    room_guest[room_number] = guest
    confirmed_guests.append(guest)

    total_revenue += price

    print("Room Booked Successfully.")

    if len(available_rooms) == 0:
        print("Hotel is Fully Booked.")
        break

print("\nRoom Guest Map")

for i in room_guest:
    print(i, "->", room_guest[i])

print("\nConfirmed Guests")

for i in confirmed_guests:
    print(i)

print("\nTotal Revenue =", total_revenue)