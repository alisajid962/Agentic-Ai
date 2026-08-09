def add(a,b):
    print("The sum of the numbers are: ",a+b)
def subtract(a,b):
    print("The Diffrence of the numbers are:",a-b)
def multiply(a,b):
    print("The multiplication of the numbers are ",a*b)
def divide(a,b):
    print("the division of the numbers are ",a/b)
is_running=True
while True:
 
      a=int(input("Enter the First Number: "))

      opr=input("Enter The opr: ")

      b=int(input("Enter the second Number: "))
 
      if opr=="+":
          add(a,b)
      elif opr=="-":
          subtract(a,b)
      elif opr=="/":
           if b==0:
             print("Undefine Cannot divide by zero")
      elif opr == "*":
         multiply(a,b)
 
 

