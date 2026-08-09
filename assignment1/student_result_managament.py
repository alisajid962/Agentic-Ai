student_data_list=[]
name = input("Enter the name of the student: ")
while  name!="stop":
    inner_student=[]
    inner_student.append(name)
    for i in range(0,5):
        marks= int(input(f"Enter the marks for {name}"))
        if (-1<marks<101):
            inner_student.append(marks)
        else:
            continue
    student_data_list.append(inner_student)
    name = input("Enter the name of student: ")
print(student_data_list)
# =====Average===grade=Pass==fail
no_of_passed_student=0
no_of_failed_student=0
for student in student_data_list:
       
        name=student[0]
        no_of_subjects=0
        sum=0
        for student_marks in student[1:]:
            no_of_subjects=no_of_subjects+1
            sum = sum+student_marks
        if no_of_subjects!=0:
            grade=None
            average=sum/no_of_subjects
            print(f"The average marks of {name} is ", average  )
            if average>=90:
                grade="A"
            elif 75<=average<90:
                grade="B"
            elif 60<=average<75:
                grade="C"
            elif 40<=average<60:
                grade="D"
            else:
                grade="F"
        print(f"The total numbers of {name} is: ",sum)
        print(f"The {name} obtained: {grade} Grade")
        if average>=40:
            print(f" {name} is Passed")
            no_of_passed_student=no_of_passed_student+1
            print("============")
        else:
            print(f" {name} is failed")
            print("============")
            no_of_failed_student=no_of_failed_student+1
print(f"Total no of passed student: {no_of_passed_student}")
print(f"Total no failed Student:  {no_of_failed_student}")

        


    
            



                

            


