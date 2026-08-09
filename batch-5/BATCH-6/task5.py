# name="Ali Sajid"

# print(name.upper())
# print(name.lower())
# print(len(name))

# info="abc4de6f"
# for char in info:
#     if char.isdigit():

#         print("digit found")


# user_input=input("Enter The chracter: ")

# if user_input in info:


#     print("Charcter is found")
# else:
#     print("Chracter not found.")
# user_input= ali1ei@byt
user_input=input("Enter the sentence: ")
vowels: int=0
digits: int=0
other:  int=0

for char in user_input:
    if char in "aeiou":
        vowels=vowels+1
    elif char.isdigit():
        digits=digits+1
    else:
        other=other+1

print(f"Vowels: {vowels} | Digits: {digits} | Others: {other}")










