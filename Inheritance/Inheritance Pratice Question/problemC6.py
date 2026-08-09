class Animal:
    def __init__(self,name):
        self.name = name

class Bird(Animal):
    def __init__(self, name,can_fly):
        super().__init__(name)
        self.canfly = can_fly


class Parrot(Bird):
    def __init__(self, name, can_fly,color):
        super().__init__(name, can_fly)
        self.color=color

    def details(self):
        print(self.color,self.canfly,self.name)

ob =Parrot("Love birds" , True,"Yellow")
ob.details()
