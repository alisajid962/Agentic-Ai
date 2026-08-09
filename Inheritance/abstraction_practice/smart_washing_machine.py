from time import sleep
class SmartWashingMachine:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
        self._is_running=False
        self._door_locked=False


    def lock_door(self):
        if  self._door_locked==True:
            print("Door Already Locked. ")
            return
        else:
            self._door_locked=True


    def unlock_door(self):
        if self._door_locked==False:
            print("Door Already Unlocked. ")
        else:
            self._door_locked=False


    def _run_wash_cycle(self):
        timimg=0
        for i in range(5):
            sleep(1)
            timimg+=1
            print(f"Machine running for {timimg}")
        self._is_running=False
        self._door_locked=False

    def start_wash(self):
        if(self._is_running):
            print("Machine Already running. ")
            return
        elif(self._door_locked==False):
            print("Please lock the door first")
            return   
        elif (self._door_locked):
            self._run_wash_cycle()
            print(f"Clothes has been washed and door are open now.")
        else:
            print(f"Some Error has been happened in {self.brand},{self.model}")
orient=SmartWashingMachine("Orient","ZX100")
orient.lock_door()
orient.start_wash()
orient.unlock_door()




        


