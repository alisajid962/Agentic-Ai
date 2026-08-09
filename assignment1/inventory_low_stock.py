products=[]
stocks=[]
reorder_products=[]
no_of_products=int(input("How many products you wnat to audit: "))
for i in range(no_of_products):
    product=input("Enter the productn name: ")
    stock = int(input(f"Enter the quantity of {product}: "))
    if stock==-1:
        continue
    elif (stock<-1 ):
        break
    elif (0<stock<10):
        reorder_products.append(product)
        print(f"The quantity of {product} is low")
    elif (10<stock):
        products.append(product)
        stocks.append(stock)
    else:
        print(f"Invalid Input")
        continue
print(f"Reorder List: {reorder_products}")
print(f"No OF Check Products: {len(products)}")
print(f"The Check Products: {products}")
print(f"Checked Products Stocks: {stocks}")
