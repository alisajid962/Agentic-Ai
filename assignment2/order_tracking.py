order_dict = {}

delivered_set = set()

processed_orders = []

total_amount = 0

while True:

    order_id = input("Enter Order ID: ").upper()

    status = input("Enter Status: ").lower()

    amount = int(input("Enter Amount: "))

    if amount < 0:
        print("Fraud Order Found")
        break
    if status == "cancelled":
        print("Order Cancelled")
        continue

    if amount > 0:
        order_dict[order_id] = status

    else:
        order_dict[order_id] = "Invalid"

    order_tuple = (order_id, amount)

    processed_orders.append(order_tuple)

    if status == "delivered":
        delivered_set.add(order_id)

    if amount > 0:
        total_amount += amount


print("\nOrder Status")

for order, status in order_dict.items():
    print(order, ":", status)

print("\nDelivered Orders")
print(delivered_set)

print("Processed Orders")

for order in processed_orders:
    print(order)
print("Total Valid Amount:", total_amount)