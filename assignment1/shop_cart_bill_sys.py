items = ["Rice","Sugar", "Oil", "Milk", "Tea","Flour", "Eggs", "Chicken"]
prices = [350,180,1200,280,950,0,420,1500]
budget = int(input("Enter the Budget: "))
final_bill=0
price_of_item=-1
total_discount=0
purschased_items=[]
item  =  input("Enter the item name: ")
while item!="stop":
    if item in items:
        index_of_item=items.index(item)
    else:
        print("item is not present")
        break
    price_of_item=prices[index_of_item]
    purschased_items.append(item)
    if( price_of_item<=budget) and (price_of_item>0):
        if price_of_item>1000:
            discount=price_of_item*0.10
            total_discount=total_discount+discount
            price_of_item=price_of_item-discount
            final_bill=final_bill+price_of_item
            budget=budget-price_of_item
        else:
            final_bill=final_bill+price_of_item
            budget=budget-price_of_item
        item  =  input("Enter the item name: ")
    elif price_of_item>budget:
        print("Bugdet exceeded")
        break
    else:
        print("invalid input")
        break

print(f"the total items: {purschased_items} ")
print(f"Total amount of items purchased: ",fin)
print(f"Total Discount: {total_discount}")
print(f"Remaining Bugdet: {budget}")





        

    