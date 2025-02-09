#The Farm class need an __init__ method with farm_name like parameter. The Farm class need 5 methods.
class Farm:
    def __init__(self, farm_name):
        self.farm_name = farm_name
        self.animals = {}

    def add_animal(self, animal, count=1):
        # If the animal already exists, increase the count, else add it. Interesting fact,We can add an animal with or without specifying a quantity. 
        if animal in self.animals:
            self.animals[animal] += count
        else:
            self.animals[animal] = count

    def get_info(self):
        # Format the farm info
        farm_info = f"{self.farm_name}'s farm\n"
        for animal, count in sorted(self.animals.items()):
            farm_info += f"{animal} : {count}\n"
        farm_info += "\n    E-I-E-I-0!"
        return farm_info
    
    def get_animal_types(self):
        # Return a sorted list of animal types
        return sorted(self.animals.keys())

    def get_short_info(self):
        # Get the list of animal types
        animal_types = self.get_animal_types()

        # Pluralize the animal names if there are more than one
        animal_names = [f"{animal}s" if self.animals[animal] > 1 else animal for animal in animal_types]

        # Construct the sentence
        animal_names_str = ', '.join(animal_names)
        return f"{self.farm_name}'s farm has {animal_names_str}."


# Example usage:
macdonald = Farm("McDonald")
macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
print(macdonald.get_info())
print(macdonald.get_info())
print(macdonald.get_short_info())
print(macdonald.get_animal_types())