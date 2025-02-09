class Zoo:
    def __init__(self, zoo_name):
        self.name = zoo_name
        self.animals = []

    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)

    def get_animals(self):
        print(f"Animals in {self.name}: {', '.join(self.animals)}")

    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)

    def sort_animals(self):
        sorted_animals = {}
        self.animals.sort()
        for animal in self.animals:
            first_letter = animal[0].upper()
            if first_letter not in sorted_animals:
                sorted_animals[first_letter] = []
            sorted_animals[first_letter].append(animal)
        return sorted_animals
    
    def get_groups(self):
        sorted_animals = self.sort_animals()
        for letter, animals in sorted_animals.items():
            print(f"Group {letter}: {', '.join(animals)}")

ramat_gan_safari = Zoo("Ramat Gan Safari")
ramat_gan_safari.add_animal("Giraffe")
ramat_gan_safari.add_animal("Bear")
ramat_gan_safari.add_animal("Baboon")
ramat_gan_safari.add_animal("Cougar")
ramat_gan_safari.add_animal("Cat")
ramat_gan_safari.add_animal("Ape")
ramat_gan_safari.add_animal("Eel")
ramat_gan_safari.add_animal("Emu")
ramat_gan_safari.sell_animal("Cougar")
ramat_gan_safari.get_animals()
print(ramat_gan_safari.sort_animals())
ramat_gan_safari.get_groups()