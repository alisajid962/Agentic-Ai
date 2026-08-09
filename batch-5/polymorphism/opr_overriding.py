class student:
    def __init__(self,name,mark1):
        self.name=name
        self.mark1=mark1
        
    def display(self):
        print(f"{self.name} got {self.mark1}")
    def __add__(self,other):
          return self.mark1+other.mark1
    def __str__(self):
         return( self.name,self.mark1)
ali=student("ali",11)
ali.display()
zain=student("zain",33)
zain.display()
print(ali)
        