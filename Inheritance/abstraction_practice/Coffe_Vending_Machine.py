from time import sleep
class CoffeeMachine:
    def __init__(self, brand):
        self.brand = brand
        self._water_heated = False
        self._coffee_level = 100

    def _heat_water(self):
        print("Heating Water...")

        for i in range(1, 5):
            sleep(1)
            print(f"Heating Stage {i}")

        self._water_heated = True
        print("Water Heated Successfully")

    def select_coffee(self, coffee_type):

        if self._coffee_level <= 0:
            print("Coffee Finished. Please Refill.")
            return

        if self._water_heated == False:
            self._heat_water()

        print(f"Preparing {coffee_type} Coffee...")
        sleep(2)

        self._coffee_level -= 20

        print(f"{coffee_type} Coffee is Ready.")
        print(f"Coffee Level Left : {self._coffee_level}%")

    def refill_coffee(self):
        self._coffee_level = 100
        print("Coffee Refilled Successfully.")


machine = CoffeeMachine("orient")
machine.select_coffee("Latte")
# print()
# machine.select_coffee("Espresso")
# print()
# machine.select_coffee("Cappuccino")
# print()
# machine.select_coffee("Mocha")
# machine.refill_coffee()
# machine.select_coffee("Mocha")
# machine.select_coffee("Mocha")