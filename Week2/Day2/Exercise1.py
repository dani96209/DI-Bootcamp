class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'
    
class Siamese(Cat):
    def sing(self, sounds):
        return f'{sounds}'

bengal_one=Bengal("Rox",12)
Chartreux_one=Chartreux("Rocky",10)
siamese_one=Siamese("Rex",8)
all_cats=[bengal_one,Chartreux_one,siamese_one]
saras_pets=Pets(all_cats)
saras_pets.walk()