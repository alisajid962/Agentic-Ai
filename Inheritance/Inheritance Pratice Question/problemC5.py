class Device:
    def power_on(self):
        print("Device Power On")

class Computer(Device):
    def run_os(self):
        print("Operating system running ")
class Laptop(Computer):
    def fold(self):
        print("Laptop Folded")


ob = Laptop()
ob.fold()
ob.power_on()
ob.run_os()
