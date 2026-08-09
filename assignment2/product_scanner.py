product_quantity = {}
unique_products = set()
all_scans = []
no_of_scans = int(input("Enter Number of Scans: "))
for i in range(no_of_scans):
    barcode = input("Enter Barcode: ")
    if barcode == "SHIFT_END":
        print("Scanning Stopped.")
        break
    product = input("Enter Product Name: ")
    scan = (barcode, product)
    barcode = scan[0]
    product = scan[1]
    if barcode == "":
        print("Unreadable Barcode.")
        continue
    if product == "":
        print("Invalid Product Name.")
        continue
    if product in product_quantity:
        product_quantity[product] += 1
    else:
        product_quantity[product] = 1
    unique_products.add(product)
    all_scans.append(scan)

    print("Product Scanned Successfully.")
print("\nProduct Quantity")
for i in product_quantity:
    print(i, "=", product_quantity[i], end=" ")
    if product_quantity[i] <= 2:
        print("(Low Stock)")
    elif product_quantity[i] <= 5:
        print("(Medium Stock)")
    else:
        print("(High Stock)")
print("Unique Products =", len(unique_products))
print("All Scans")
for i in all_scans:
    print(i)
