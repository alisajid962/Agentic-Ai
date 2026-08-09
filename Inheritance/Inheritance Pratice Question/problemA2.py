class Shape:
    def __init__(self):
        pass

    def info(self):
        print("This is a Shape")

class Circle(Shape):
    def __init__(self,radius):
        super().__init__()
        self.radius = radius

    def area(self):
        print("Area " , self.radius * 3.14)

Cir = Circle(5)

Cir.info()
Cir.area()
