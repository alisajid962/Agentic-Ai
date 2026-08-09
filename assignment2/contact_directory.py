cont_dict={}
name_set=set(cont_dict.keys())
order_list=[]
name=input("Enter name: ").lower()
count=0
while name!="exit":
    if name=="":
        name=input("Enter the name: ").lower()
        continue
    if name in name_set:
        name=input("Enter the name: ").lower()
        continue
    name_num_tuple=()
    number= input("Enter number: ")
    if len(number)!=11:
       print(f"invalid numer: {number}")
      
       continue
    
    cont_dict[name]=number
    name_num_tuple=(name,number)
    name_set.add(name)
    order_list.extend(name_num_tuple)
    count+=1
    name=input("Enter the name: ").lower()
print(f"Contac: {cont_dict}")
print(f"Unique contact: {name_set}")





