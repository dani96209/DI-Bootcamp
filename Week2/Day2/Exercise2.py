class Dog():
    def __init__(self,name,age,weight):
        self.name=name
        self.age=age
        self.weight=weight
    
    def bark(self):
        print(f"{self.name} is barking")
    
    def run_speed(self):
        return (self.weight/self.age)*10

    def fight(self,other_dog):
        self_strong = self.run_speed() * self.weight
        other_strong = other_dog.run_speed() * other_dog.weight
        if self_strong > other_strong:
            return f"{self.name} wins the fight!"
        elif self_strong < other_strong:
            return f"{other_dog.name} wins the fight!"
        else:
            return "It's a tie!"
        
dog_1 = Dog("Rex", 5, 20)
dog_2 = Dog("Django", 3, 18)
dog_3 = Dog("Rocky", 4, 22)

print(dog_1.fight(dog_2))