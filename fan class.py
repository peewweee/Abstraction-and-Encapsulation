# Designing a class named Fan to represent a fan
# Phoebe Rhone L. Gangoso | BSCpE 1-4

# PSEUDOCODE
class Fan:
    # constants for fan speeds
    SLOW = 1
    MEDIUM = 2
    FAST = 3
    # constructor for initializing the Fan object
    def __init__(self, speed=1, radius=5, color='blue', on=False):
        self.__speed = speed
        self.__on = on
        self.__radius = radius
        self.__color = color
# getter and setter methods for speed
# for radius
# for color
# for on