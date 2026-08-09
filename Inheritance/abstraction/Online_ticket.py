from abc import ABC,abstractmethod
class Ticket(ABC):
    def __init__(self,amount):
        self.amount=amount 
    @abstractmethod
    def validate_ticket():
        pass
    @abstractmethod
    def calculate_price(self):
        pass

    def book_ticket(self):
        print(f"{self.amount} pkr Ticket is booked")
class MovieTicket(Ticket):
    def __init__(self, amount):
        super().__init__(amount)
    def validate_ticket(self):
        if self.amount>0:
            print(F"Ticket is validated")
        else:
            print("Ticket is not validated. ")
  
    def book_ticket(self):
       print(F"A  ticket of {self.amount} is booked for movie ")
class BusTicket(MovieTicket):
    def __init__(self,amount):
        super().__init__(amount)
    def validate_ticket(self):
          if self.amount>0:
                print(F"Ticket is validated")
          else:
                print("Ticket is not validated. ")
    def _calculate_price(self):
        self.tax=self.amount*0.15
        self.amount+=self.tax
        print(f"Total Amount Including taxes: {self.tax}")

    def book_ticket(self):
           print(F"A  ticket of {self.amount} is booked for Bus ")
    
         
niazi=BusTicket(1000)
niazi.validate_ticket()
niazi.validate_ticket()
        
        




