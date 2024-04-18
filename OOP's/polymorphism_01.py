#

def PetLover(pet):
    pet.talk()
    if hasattr(pet,'walk'):     # 'hasattr()' is a function to check whether attribute is present or not 
        pet.walk()

class Duck:
    def talk(self):
        print('Duck is Talking')

    def walk(self):
        print('Duck is walking')

class Dog:
    def talk(self):
        print('Dog is talking')


dk = Duck()     # Duck object created
PetLover(dk)    # Calling Petrover function and passing dk object of Duck() as parameter

print()

dg = Dog()
PetLover(dg)