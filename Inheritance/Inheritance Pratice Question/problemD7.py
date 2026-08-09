class Employe:
    def __init__(self,name):
        self.name =name

    def show_name(self):
        pass

class Manager(Employe):
    def __init__(self, name):
        super().__init__(name)

    def conduct_meeting(self):
        print(self.name,"is conducting a meeting")

class Developer(Employe):

    def write_code(self):
        print(self.name,"is Writing Code")


ob1 = Manager("Muneeb")
ob2 = Developer("Ahmad")

ob1.show_name()
ob1.conduct_meeting()

ob2.show_name()
ob2.write_code()
