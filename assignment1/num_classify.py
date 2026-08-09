numbers=[1,22,44,33,4,5,6,7,89,90,29,0,2,0,22,11,12,14,15,9,-999,67,54,45]
even=[]
odd=[]
prime=[]
for num in numbers:
    if  num>1:
        is_prime=True
        for i in range(2,num):
            if num%i==0:
                is_prime=False
                break
        if is_prime:
            prime.append(num)
    if num==0:
        continue
    elif num==-999:
        break
    elif (num%2==0):
        even.append(num)
    elif (num%2!=0):
        odd.append(num)
    else:
        continue
print(f"total no of evens:  {len(even)}")
print(even)
print("-----------------------------")
print(f"total no of odd are: {len(odd)}")
print(odd)
print("------------------------------------")
print(f"total no prime are:  {len(prime)}")
print(prime)
    

