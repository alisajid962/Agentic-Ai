from time import sleep

class TrafficLight:

    mapping = {
        "red": 5,
        "yellow": 2,
        "green": 4
    }

    def __init__(self, location):
        self.location = location
        self._current_color = "red"

    def __countdown_timer(self, color):
        seconds = self.mapping[color]

        while seconds > 0:
            print(f"{seconds} seconds remaining before switching to {color}")
            sleep(1)
            seconds -= 1

    def change_to(self, color):

        if color not in self.mapping:
            print("Invalid Color")
            return

        if color == self._current_color:
            print(f"Traffic Light is already {color}")
            return

        print(f"\nChanging from {self._current_color} to {color}...\n")

        self.__countdown_timer(color)

        self._current_color = color

        print(f"Traffic Light changed to {self._current_color}\n")

signal = TrafficLight("COMSATS Gate")
signal.change_to("green")
signal.change_to("yellow")
signal.change_to("red")
signal.change_to("blue")
signal.change_to("red")