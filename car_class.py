# Car Class to display current speed of car
# Phoebe Rhone L. Gangoso | BSCpE 1-4

# PSEUDOCODE
# class car
class Car:
    def __init__(self, year_model, make):
    # initialize car object (speed attribute = 0)
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0

    # accelerate method
    def accelerate(self):
        self.__speed += 5

    # brake method
    def brake(self):
        self.__speed -= 5

    # get_speed method
    def get_speed(self):
        return self.__speed

    # print make and year model
    def show(self):
        print("\N{automobile} Your Car:", self.__make)
        print("\N{wrench} Year Manufactured:", self.__year_model)