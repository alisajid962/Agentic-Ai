class Person:
    def __init__(self,name):
        self.name  = name

    def introduce(self):
        print(f"Hi {self.name}")

class Student(Person):
    def __init__(self, name):
        super().__init__(name)

    def study(self):
        print(self.name,"is Studying")

std1 = Student("Muneeb")

std1.introduce()
std1.study()
