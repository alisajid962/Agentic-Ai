from time import sleep
class ATMMachine:
    def __init__(self,bank_name):
        self.bank_name=bank_name
        self._pin=1122
        self._balance=10000
        self._card_inserted=False
        self._pin_verified=False
    def insert_card(self):
        if(self._card_inserted):
            print("Card Already Inserted. ")
        else:
            self._card_inserted=True
    def enter_pin(self,inp_pin):
        if(self._pin==inp_pin):
            self._pin_verified=True
        else:
            print(f"Incorrect pin {inp_pin}")
            return
    def _dispense_cash(self,amount):
        if(0<amount<5000):
          
            for i in range(2):
                sleep(1)
                print("Calculating Cash in Cash Counter. ")
            print(f"{amount} has been given")
        elif(5000<amount<10000):
            for i in range(3):
                sleep(3)
                print("Calculating Cash in Cash Counter. ")
            print(f"{amount} has been given")
        else:
                for i in range(5):
                    sleep(3)
                    print("Calculating Cash in Cash Counter. ")
                print(f"{amount} has been given")
    def withdraw(self,amount):
        if amount<0 or self._balance<amount:
            print(f"Invalid Amount: {amount}")
        elif(self._card_inserted==False):
            print("Please Insert Card First. ")
            return
        elif(self._pin_verified==False):
            print(f"Please Verify Pin First. ")
            return
        else:
            self._balance-=amount
            self._dispense_cash(amount)
            print(f"Account Balance: {self._balance}")
hbl=ATMMachine("hbl")
hbl.insert_card()
hbl.enter_pin(1122)
hbl.withdraw(1000)



        

    


        