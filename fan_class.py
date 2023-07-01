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
    def get_speed(self):
        return self.__speed

    def set_speed(self, speed):
        self.__speed = speed

    # for radius
    def get_radius(self):
        return self.__radius

    def set_radius(self, radius):
        self.__radius = radius

    # for color
    def get_color(self):
        return self.__color

    def set_color(self, color):
        self.__color = color

    # for on
    def is_on(self):
        return self.__on

    def set_on(self, on):
        self.__on = on