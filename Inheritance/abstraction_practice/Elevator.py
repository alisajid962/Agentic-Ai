from time import sleep
class Elevator:
    total_floors=20
    def __init__(self,building_name):
        self.building_name=building_name
        self._current_floor=9
        self._door_open=False
        self._moving=False
    def _open_door(self):
        if (self._door_open==True):
            print(f"Door Already open. ")
        elif(self._moving):
            print("Cannot open Doors During Moving")
        else:
            self._door_open=True
            print("Door opened")
    def _close_door(self):
        if (self._door_open==False):
            print(f"Door Already Closed")
        else:
            self._door_open=False
            print("Door closed")
    def _move_to_floor(self,floor):
        if self._current_floor==floor:
            print(f"You are already on floor: {self._current_floor}")
        elif (floor>self._current_floor):
            while self._current_floor!=floor:
                sleep(1)
                self._current_floor+=1
                print(f"Going up on {self._current_floor}")
        else:
            while self._current_floor!=floor:
                sleep(1)
                self._current_floor-=1
                print(f"Going Down on {self._current_floor}")
    def go_to_floor(self,floor):
        if (floor>self.total_floors):
            print("Floors Out of range")
            return
        if (self._moving):
            print("Already Moving. ")
            return
        if(self._door_open==True):
             self._close_door()
        self._moving=True
        self._move_to_floor(floor)
        print(f"You are now at floor : {floor}")
        self._moving=False
        self._open_door()
hsp=Elevator("hsp")
hsp.go_to_floor(3)
hsp._open_door()
        
            





    
