student_courses = {}

course_seats = {
    "AI": 2,
    "WEB": 2,
    "DB": 2
}

registration_list = []

count = 0
quota = 3



while True:

    if count == quota:
        print("Registration Quota Full")
        break

    student = input("Enter Student Name: ").lower()

    course = input("Enter Course (AI/WEB/DB): ").upper()

    registration = (student, course)

    if student not in student_courses:
        student_courses[student] = set()

    if course in student_courses[student]:
        print("Student already registered in this course")
        continue
    if course_seats[course] > 0:
        student_courses[student].add(course)
        course_seats[course] -= 1
        registration_list.append(registration)
        count += 1
        print("Registration Successful")

    else:
        print("No Seats Left")


print("Student Courses")

for student, courses in student_courses.items():
    print(student, ":", courses)
print("Remaining Seats")
for course, seats in course_seats.items():
    print(course, ":", seats)
print("\nRegistrations")
for reg in registration_list:
    print(reg)
student1 = input("\nEnter First Student: ").lower()
student2 = input("Enter Second Student: ").lower()
if student1 in student_courses and student2 in student_courses:
    common = student_courses[student1] & student_courses[student2]
    print("Common Courses:", common)
else:
    print("Student Not Found")