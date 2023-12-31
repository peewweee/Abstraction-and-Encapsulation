# Pet Class
# Phoebe Rhone L. Gangoso | BSCpE 1-4

# PSEUDOCODE
# class pet
class Pet:
    def __init__(self):
        # initialize attributes
        self.__name = ""
        self.__animal_type = ""
        self.__age = 0

# set_name method
    def set_name(self, name):
        self.__name = name

# set_animal_type method
    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type

# set_age method
    def set_age(self, age):
        self.__age = age

# get_name method
    def get_name(self):
        return self.__name

# get_animal_type method
    def get_animal_type(self):
        return self.__animal_type

# get_age method
    def get_age(self):
        return self.__age