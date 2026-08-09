slot_vehicle_dict = {}

occupied_slots = set()
reserved_slots = {2, 5}
parked_vehicle_list = []

total_slots = 6

while True:

    if len(occupied_slots) == total_slots - len(reserved_slots):
        print("Parking Full")
        break

    vehicle_number = input("Enter Vehicle Number: ").upper()

    requested_slot = int(input("Enter Slot Number: "))

    vehicle_tuple = (vehicle_number, requested_slot)
    if requested_slot in reserved_slots:
        print("Reserved Slot")
        continue
    if requested_slot not in occupied_slots:
        occupied_slots.add(requested_slot)
        slot_vehicle_dict[requested_slot] = vehicle_number
        parked_vehicle_list.append(vehicle_tuple)
        print("Vehicle Parked")
    else:
        print("Slot Already Occupied")
print("Slot -> Vehicle")

for slot, vehicle in slot_vehicle_dict.items():
    print(slot, ":", vehicle)

print("Parked Vehicles")

for vehicle in parked_vehicle_list:
    print(vehicle)
free_slots = total_slots - len(occupied_slots) - len(reserved_slots)
print("Free Slots:", free_slots)