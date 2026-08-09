# num_int = int("100")
# print(type(num_int),num_int) 

complex_number=4+4j
print(complex_number.real)
print(type(complex_number))
name="Ali sajid"
# """this function is used to calculate the percentage""" docstring

students=["Ali Sjaid","zain","Ahmed"]
studnet1={
    "name":"Bilal",
    "Course":"Agentic Ai"
}

# ===
# print(studnet1)
# print(type(studnet1))
# # ==================bytes
# chars=[65, 66, 67, 69]
# byte_array: bytearray = bytearray(chars) #65=A, 66=B ....decimal number system
# print(type(byte_array), byte_array)  # <class 'bytearray'>
# print(byte_array[0])
# print(chr(byte_array[0]))
# print("Empty bytearray(): ",bytearray())

# # ==============================
# a=10
# b=10
# print(id(a))
# print(id(b))
# b=19
# print(id(b))


# num=20
# print(type(num))
# ============explicit type casting
# num=float("10")
# print(type(num),num)
# =================implicit type casting
# x=12
# y=2
# # +,-,/,* operators
# ans=x/y
# ====
# print(type(ans),ans)





sentence = input("Enter a sentence: ")


vowels = 0
digits = 0
others = 0

for ch in sentence:
    if ch.lower() in "aeiou":
        vowels += 1
    elif ch.isdigit():
        digits += 1
    else:
        others += 1


print("Vowels:", vowels)
print("Digits:", digits)
print("Other Characters:", others)

# ===============================
# # Take input from the user
# n = int(input("Enter a number: "))

# # Variable to store the sum
# total = 0

# # Loop from 1 to n
# for i in range(1, n + 1):
#     total = total + i

# # Display the result
# print("Sum =", total)