#Packages to be imported

#Class defination starts

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

#Class defination ends

"""Factory Method"""

def get_pet(pet_key='Dog'):
    # Dog will be default value of the pet_key
        
    #First way of implementation
    """
    if pet_key == 'Cat':
        return Cat(pet_name)
    else:
        return Dog(pet_name)
    """

    #Second way of implementation
    pets = dict(dog=Dog('Brad'), cat=Cat('Tom'))
    return pets[pet_key]

"""object creation"""
obj1 = get_pet('cat')
print(obj1._name+" does "+obj1.speak())

obj2 = get_pet('dog')
print(obj2._name+" does "+obj2.speak())

