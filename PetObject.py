# Pet Object
# Phoebe Rhone L. Gangoso | BSCpE 1-4

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
# display data