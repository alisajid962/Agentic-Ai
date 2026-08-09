from time import sleep
class SmartThermostat:
    def __init__(self, location):
        self.location = location
        self._current_temp = 25
        self._target_temp = 25
        self._mode = "Idle"

    def _adjust_temperature(self):

        if self._current_temp < self._target_temp:

            while self._current_temp != self._target_temp:
                sleep(1)
                self._current_temp += 1
                print(f"Heating... Temperature is {self._current_temp}°C")

        elif self._current_temp > self._target_temp:

            while self._current_temp != self._target_temp:
                sleep(1)
                self._current_temp -= 1
                print(f"Cooling... Temperature is {self._current_temp}°C")

        self._mode = "Idle"
        print("Target Temperature Reached.")
        print("Thermostat is now Idle.")

    def set_temperature(self, temp):

        self._target_temp = temp

        if self._current_temp == self._target_temp:
            print(f"Temperature is already {self._current_temp}°C")
            return

        elif self._target_temp > self._current_temp:
            self._mode = "Heating"
            print("Mode :", self._mode)

        else:
            self._mode = "Cooling"
            print("Mode :", self._mode)

        self._adjust_temperature()


room = SmartThermostat("Bedroom")
room.set_temperature(30)
print()
room.set_temperature(22)
print()
room.set_temperature(22)