customer_points = {}
premium_customers = set()
processed_customers = []
premium_threshold = int(input("Enter Premium Spending Threshold: "))
reward_budget = int(input("Enter Total Reward Budget: "))
no_of_purchases = int(input("Enter Number of Purchases: "))
total_points = 0

for i in range(no_of_purchases):

    customer = input("Enter Customer Name: ")
    amount = int(input("Enter Amount Spent: "))

    purchase = (customer, amount)
    customer = purchase[0]
    amount = purchase[1]
    if amount == 0:
        print("Purchase Skipped.")
        continue
    if amount < 0:
        print("Invalid Purchase Amount.")
        continue
    if amount > 2000:
        points = amount * 3

    elif amount > 500:
        points = amount * 2

    else:
        points = amount
    if total_points + points > reward_budget:
        print("Reward Budget Exceeded.")
        break
    if customer in customer_points:
        customer_points[customer] += points
    else:
        customer_points[customer] = points
    if customer not in processed_customers:
        processed_customers.append(customer)
    if amount >= premium_threshold:
        premium_customers.add(customer)
    if customer_points[customer]>premium_threshold:
        premium_customers.add(customer)

    total_points += points

    print("Points Awarded Successfully.")

print("Customer Points")
for i in customer_points:
    print(i, "=", customer_points[i])

print("fProcessed Customers")
for i in processed_customers:
    print(i)
print("\nPremium Customers")
for i in premium_customers:
    print(i)
print("\nTotal Reward Points Awarded =", total_points)