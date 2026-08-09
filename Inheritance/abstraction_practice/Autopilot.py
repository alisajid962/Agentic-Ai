from time import sleep

class AutopilotSystem:

    def __init__(self, flight_number):
        self.flight_number = flight_number
        self._altitude = 0
        self._target_altitude = 0
        self._autopilot_on = False

    def engage_autopilot(self, target_altitude):

        if self._autopilot_on:
            print("Autopilot is already ON")
            return

        self._autopilot_on = True
        self._target_altitude = target_altitude

        print(f"Autopilot Engaged for Flight {self.flight_number}")
        print(f"Target Altitude: {self._target_altitude} ft\n")

        self.__adjust_altitude()

    def disengage_autopilot(self):
        self._autopilot_on = False
        print("\nAutopilot Disengaged")

    def __adjust_altitude(self):

        while self._autopilot_on and self._altitude != self._target_altitude:

            if self._altitude < self._target_altitude:

                self._altitude += 1000

                if self._altitude > self._target_altitude:
                    self._altitude = self._target_altitude

                print(f"Climbing... Current Altitude: {self._altitude} ft")

            else:

                self._altitude -= 1000

                if self._altitude < self._target_altitude:
                    self._altitude = self._target_altitude

                print(f"Descending... Current Altitude: {self._altitude} ft")

            sleep(1)

        if self._autopilot_on:
            print(f"\nTarget Altitude {self._target_altitude} ft Reached")


# Driver Code

plane = AutopilotSystem("PK-786")

plane.engage_autopilot(5000)

plane.disengage_autopilot()

plane.engage_autopilot(2000)