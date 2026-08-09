number= int(input("Enter the range of even numbers: "))
for i in range(1,number+1):
    if i%2!=0:
       continue
    print(i)
    