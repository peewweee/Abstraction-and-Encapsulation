# Main program to display current speed of car
# Phoebe Rhone L. Gangoso | BSCpE 1-4

import gui_Car
gui_Car.GUI()

# PSEUDOCODE
# import car class
from car_class import Car

# create car object
car_sample = Car(2023, "Toyota")

# print object
car_sample.show()

# call accelerate method 5 times
print("\n\033[0;32m Accelerating")
for _ in range(5):
    car_sample.accelerate()
    print("\033[0;37mCurrent speed:", car_sample.get_speed())

# call brake method 5 times
print("\n\033[0;31m Braking")
for _ in range(5):
    car_sample.brake()
    print("\033[0;37mCurrent speed:", car_sample.get_speed())