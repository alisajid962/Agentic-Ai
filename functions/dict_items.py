my_dict={
    "Chery":1,
    "Apple":2,
    "Banana":3
}
sorted_dict=dict(sorted(my_dict.items(),key=lambda item: item[1]))
print(sorted_dict)
