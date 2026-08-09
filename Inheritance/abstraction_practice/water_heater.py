import time

class FitnessTracker:
    def __init__(self, user_name):

        self.user_name = user_name
        self._workout_active = False
        self._steps = 0
        self._calories = 0

    def start_workout(self):
  
        if self._workout_active:
            print(f"[{self.user_name}] Workout is already active!")
        else:
            self._workout_active = True
            print(f"[{self.user_name}] Starting workout session...")
            self._track_workout()

    def stop_workout(self):
 
        if self._workout_active:
            self._workout_active = False
            print(f"[{self.user_name}] Workout stopped manually.")
            print(f"--- Workout Summary for {self.user_name} ---")
            print(f"Total Steps: {self._steps}")
            print(f"Total Calories Burned: {self._calories:.1f}")
        else:
            print(f"[{self.user_name}] No active workout to stop.")

    def _track_workout(self):
     
        for second in range(1, 6):
            if not self._workout_active:
                break
                
            time.sleep(1)
            
        
            self._steps += 3  
            self._calories += 0.2  
            
            print(f"[{self.user_name}] Tracking... Second {second}/5 | Steps: {self._steps} | Calories: {self._calories:.1f}")

       
        if self._workout_active:
            self._workout_active = False
            print(f"\n[{self.user_name}] Workout finished automatically!")
            print(f"--- Final Workout Summary for {self.user_name} ---")
            print(f"Total Steps: {self._steps}")
            print(f"Total Calories Burned: {self._calories:.1f}\n")
if __name__ == "__main__":
    tracker = FitnessTracker(user_name="Alex")
    tracker.start_workout()
    tracker.stop_workout()
    tracker.start_workout()