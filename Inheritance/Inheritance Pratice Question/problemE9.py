class Vehicle:
    def describe(Self):
        print("Vehicle")

class LandVehicle(Vehicle):
    def describe(Self):
        print("Land Vehicle")
        super().describe()

class WaterVehicle(Vehicle):
    def describe(Self):
        print("Water Vehicle")
        super().describe()

class AmphibiousVehicle(LandVehicle,WaterVehicle):
    def describe(Self):
        print("Amphibious")
        return super().describe()

ob = AmphibiousVehicle()
ob.describe()
#question 10
print(AmphibiousVehicle.__mro__)


