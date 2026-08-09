class payment:
    def ___init__(self,amount):
        self.amount=amount
    def pay(self):
        print(f"{self.amount} payed in cash")
            
class jazzcash(payment):
    def __init__(self,amount):
       super().__init__(amount)
    def pay(self):
        print(f"{self.amount} is payed via jazzcash")
class creditcard(payment):
    def __init__(self,amount):
      super().__init__(amount)
    def pay(self):
        print(f"{self.amount} is payed via credit card")
class easypaisa(payment):
    def __init__(self,amount):
        super().__init__(amount)
        
    def pay(self):
        print(f"{self.amount} is payed via easypaisa")
    
ali = creditcard(1000)
ali.pay()
zain=jazzcash(2000)
zain.pay()


        
        