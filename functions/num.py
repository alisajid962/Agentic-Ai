def my_sum(*list):
    print(f"The type is {type(list)} and sum is {sum(list)}")
my_sum(1,1,1,1,1,2,2,2,2,2,)
my_sum(*[1,1,1,1,1,1,1,1,1,1,1,1,1,1])
my_sum((1,1,1,1,1,11))
