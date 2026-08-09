# name = input("Enter your name: ")
# while (name!="ali"):
#     name= input("Enter your name: ")    
# print("Welcome", name)

# =======================
# i=0
# while(i<10):
#     i=i+1
#     print(i)
# ====================================
# number = int(input("Enter the number: "))
# total_sum = 0

# while number > 0:
#     digit = number % 10
#     total_sum += digit
#     number //= 10

# print(f"The Sum  is = {total_sum}")
# ============================================
no_of_tables= int(input("Enter how many numbers you want to enter: "))
for i in range(0,no_of_tables):
    num = int(input("Enter the number "))
    j=0
    while(j<10):
        j=j+1
        print(f"{num} * {j} = {num*j}")
    

