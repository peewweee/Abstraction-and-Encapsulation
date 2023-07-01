# Main program to display current speed of car
# Phoebe Rhone L. Gangoso | BSCpE 1-4

# PSEUDOCODE
# import car class
from car_class import Car
# create car object
car_sample = Car(2023, "Toyota")
# call accelerate method 5 times
for _ in range(5):
    car_sample.accelerate()
    print("Current speed:", car_sample.get_speed())
# call brake method 5 times
for _ in range(5):
    car_sample.brake()
    print("Current speed:", car_sample.get_speed())