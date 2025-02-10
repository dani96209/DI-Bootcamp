from Exercise2 import Dog
import random
class PetDog(Dog):
    def __init__(self, name, age, weight, trained=False):
        super().__init__(name, age, weight)  # Appelle le constructeur de Dog
        self.trained = trained  # Nouvel attribut pour indiquer si le chien est dressé

    def train(self):
        """Dresse le chien en le faisant aboyer et change l'état en 'dressé'."""
        print(self.bark())  # Fait aboyer le chien
        self.trained = True  # Le chien est maintenant dressé

    def play(self, *other_dogs):
        
        dog_names = ", ".join([dog.name for dog in other_dogs])
        print(f"{self.name}, {dog_names} all play together")

    def do_a_trick(self):
        """Si le chien est dressé, il exécute un tour au hasard."""
        if self.trained:
            tricks = [
                f"{self.name} does a barrel roll",
                f"{self.name} stands on his back legs",
                f"{self.name} shakes your hand",
                f"{self.name} plays dead"
            ]
            print(random.choice(tricks))
        else:
            print(f"{self.name} is not trained yet. Train him first!")

dog_1 = PetDog("Buddy", 4, 15)
dog_2 = PetDog("Rex", 5, 20)
dog_3 = PetDog("Luna", 3, 18)

dog_1.train()
dog_1.play(dog_2,dog_3)
dog_1.do_a_trick()