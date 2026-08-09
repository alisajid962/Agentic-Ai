temp_readings=[]
freezing=[]
cold=[]
normal=[]
hot=[]

no_of_readings= int(input("Enter how many readings oyu want to enter: "))

for i in range(no_of_readings+1):
    reading=int(input("Enter the reading: "))
    if reading==-100:
        continue
    elif reading <0:
        temp_readings.append(reading)
        freezing.append(reading)
    elif(0<reading<=15):
       temp_readings.append(reading)
       cold.append(reading)
    elif (15<reading<=35):
        temp_readings.append(reading)
        normal.append(reading)
    elif (35<reading<50):
        hot.append(reading)
        temp_readings.append(reading)
    else:
        break
print(f"Freezing temprature: {len(freezing)}")
print(f"cold tempratur: {len(cold)}")
print(f"normal temprature: {len(normal)}")
print(f"Hot temprature: {len(hot)}")
highest = temp_readings[0]
for reading in temp_readings[1:]:
    if reading>highest:
        highest=reading
print(f"The highest temprature: {highest}")


