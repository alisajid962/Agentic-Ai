menu_dict = {
    "burger": 350,
    "pizza": 1200,
    "fries": 250,
    "biryani": 450,
    "drink": 150
}

sold_out_set = {"pizza"}

order_list = []

grand_total = 0

while True:

    item = input("Enter Item Name: ").lower()

    if item == "close":
        print("Kitchen Closed")
        break
    quantity = int(input("Enter Quantity: "))

    if quantity<0:
        print("Invalid quantity.  ")
        continue
    if quantity == 0:
        print("Invalid Quantity")
        continue

    if item not in menu_dict:
        print("Item Not Found")
        continue
    order_tuple = (item, quantity)
    if item in sold_out_set:
        print("Item is Sold Out")
    else:
        price = menu_dict[item] * quantity
        grand_total += price
        order_list.append(order_tuple)
        print("Item Added")


print("Itemized Bill")
for item, quantity in order_list:
    print(item, "x", quantity, "=", menu_dict[item] * quantity)

print("\nGrand Total:", grand_total)