class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print(f"{self.name} is a person")
class student(person):
    def __init__(self, name,age,roll_no):
        super().__init__(name,age)
        self.roll_no=roll_no
    def display(self):
        print(f"{self.name} is student and have {self.roll_no} Roll No")
class teacher(person):
    def __init__(self, name, age,dep):
        super().__init__(name, age)
        self.dep=dep
    def display(self):
        print(f"{self.name} is a teacher in {self.dep} Department. ")
class resarcher(teacher):
    def __init__(self, name, age,dep,thiesis_title):
        teacher.__init__(self,name,age,dep)
        self.thiesis_title=thiesis_title
    def display(self):
        print(f"{self.name} is a researcher and have thiesis title: {self.thiesis_title}")
zain=resarcher("zaiin",19,"Se","TimeComplexity")
zain.display()
