marks_eraned=[]
total_marks_list=[]
perfect_ans=0
sum=0
total_marks=0
no_of_subjects=int(input("Enter the no of subjects: "))
for i in range(no_of_subjects):
    total_marks=int(input("Enter the total marks: "))
    if total_marks==0:
        continue
    obt_marks=int(input("Enter the Obtainexd Marks: "))
    if obt_marks<=-5:
        break
    if total_marks==obt_marks:
        perfect_ans+=1
        marks_eraned.append(obt_marks)
        total_marks_list.append(total_marks)
    
   
    elif obt_marks>total_marks:
        print("Invalid marks.")
        continue
    else:
        marks_eraned.append(obt_marks)
        total_marks_list.append(total_marks)

for i in marks_eraned:
    sum+=i
for i in total_marks_list:
    total_marks+=i
percentage=(sum/total_marks)*100
if percentage>=85:
    print(f"The Grade is : Excellent")
elif  60<=percentage<85:
    print("The Grade is: Good")
elif  40<=percentage<60:
    print("The grade is: Average")
else:
    print("The Grade is: Poor")
print(f"The Total Score is: {sum} out of {total_marks}")
print(f"The percentage is: {percentage}%")
print(f"The Perfect Answeres: {perfect_ans}")







