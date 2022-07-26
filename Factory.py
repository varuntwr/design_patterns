#Packages to be imported

class Dog:

    def __init__(self, name):
        self._name = name

    def speak(self):
        return "Woof!"

class Cat:

    def __init__(self, name):
        self._name = name

    def speak(self):
        return "Meow!"

"""Factory Method"""
def get_pet(pet_key, pet_name: str):
    if pet_key == 'Cat':
        return Cat(pet_name)
    else:
        return Dog(pet_name)
    

pet_name = input("Enter the name of your pet: ")

"""Object creation"""
d1 = get_pet('Cat', pet_name)
print(type(d1))
print(d1.speak())

