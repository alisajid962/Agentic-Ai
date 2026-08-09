class  Teacher:
    def work(self):
        print("Teaching Students ")

class Writer:
    def work(self):
        print("Writing Books ")

class Author(Writer,Teacher):
    pass

ob = Author()
ob.work()

print(Author.__mro__)


#it runs the writer function because it comes first in MRO as it start from left to right

