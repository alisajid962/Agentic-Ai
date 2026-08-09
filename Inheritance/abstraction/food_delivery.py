from abc import ABC ,abstractmethod
class FoodOrder(ABC):
    def __init__(self,amount):
        self._validate_order(amount)
    def _validate_order(self,amount):
        if amount>0:
            self.amount=amount
        else:
            print("Order cant be zero")
    @abstractmethod
    def _calculate_delivery_fee(self):
        pass
    def _process_order(self):
        print(f"{self.amount} order is processing")
class RestRauntOrder(FoodOrder):
    def __init__(self, amount):
        super().__init__(amount)
    def _calculate_delivery_fee(self):
        global delivery_fee
        self.delivery_fee=self.amount*0.1
        self.amount+=self.delivery_fee
        print(f"Delivery Fees is: {self.delivery_fee}")
    def _process_order(self):
        print(f"Total Amount: {self.amount} including fees  is proccessing in Restraunt")
class Grocery(FoodOrder):
    def __init__(self, amount):
        super().__init__(amount)
    def _calculate_delivery_fee(self):
                global delivery_fee
                self.delivery_fee=self.amount*0.05
                self.amount+=self.delivery_fee
                print(f"Delivery Fees is: {self.delivery_fee}")
    def _process_order(self):
            print(f"Total Amount: {self.amount} including fees  is proccessing in Grocery")            
order1=Grocery(1000)
order1._calculate_delivery_fee()
order1._process_order()
        

    