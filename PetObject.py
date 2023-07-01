# Pet Object
# Phoebe Rhone L. Gangoso | BSCpE 1-4

import gui_Pet
gui_Pet.Header()

# PSEUDOCODE
from pet_class import Pet
# create object of the Pet class
pet = Pet ()

# input prompts (name, animal type, and age)
name = input("Enter your pet's name: ")
animal_type = input("Enter your pet's animal type: ")
age = input("Enter your pet's age: ")

# set as object attributes
pet.set_name(name)
pet.set_animal_type(animal_type)
pet.set_age(age)

# retrieve name, type, and age
pet_name = pet.get_name()
pet_animal_type = pet.get_animal_type()
pet_age = pet.get_age()

# display data
gui_Pet.Display()
print(" Name:", pet_name)
print(" Animal Type:", pet_animal_type)
print(" Age:", pet_age)