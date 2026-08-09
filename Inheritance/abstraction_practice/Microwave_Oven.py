from time import sleep
class MicrowaveOven:
    def __init__(self,brand:str):
        self.brand=brand
        self._door_closed=True
        self._is_running=False
    def open_door(self):
        if(self._is_running):
            print(" Running Cant open door()")
            return
        elif(self._door_closed==False):
            print("Doors are opened already. ")
        else:
            self._door_closed=False
    def close_door(self):
        self._door_closed=True
    def _cook(self,seconds):
        for i in range(seconds):
            sleep(1)
            print(f"Cooking...{i}")
        print(f"Cooked for {seconds}")
    def start_cooking(self,seconds):
        if(self._is_running==True):
            print(f"Oven Already Running")
            return
        elif(self._door_closed==False):
            print(f"Close the doors please...")
        else:

            self._cook(seconds)


orient=MicrowaveOven("orient")
orient.start_cooking(12)


