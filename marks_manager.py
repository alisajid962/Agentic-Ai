# ======================================================================================
marks=[]
no_of_students=-1
while  (no_of_students)<0:
       try:
          no_of_students=int(input("How many students you want to enter: "))
       except ValueError:
        print("Enter a valid number. ")
for i in range(no_of_students):
    mark=-100
    while 0>mark>100:
         mark= int(input(f"Enter the  marks of  {i+1} Student: "))
        
    if (0<mark<101):
        marks.append(mark)
    else:
        print("Invalid Marks." ,end="----\n")
        continue
for i in marks:
    print(i)
#  =================================================================
highest=marks[0]
for m in marks:
    if m>highest:
        highest=m
print("Highest marks ",highest)
#  =========================================================================
lowest=marks[0]
for n in marks:
    if n<lowest:
        lowest=n
print("Lowest Number is ",lowest)
print("Total of All Marks ",sum(marks))
print("Average  ",sum(marks)/no_of_students)





    
    


     
    

