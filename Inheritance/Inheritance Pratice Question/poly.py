class add:
   
    def __add__(self, other):
        return (self.x+other.x ,self.y+self.y)
class point(add):
    def __init__(self,x:int,y:int):
        self.x=x
        self.y=y
    def __str__(self):
        return f"{(self.x,self.y)}"
p1=point(1,1)
p2=point(1,1)
print(p1)
print(p2)
print(p1+p2)