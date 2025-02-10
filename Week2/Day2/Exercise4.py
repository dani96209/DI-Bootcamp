class Family:
    def __init__(self, last_name):
        self.members = []  # Liste vide pour les membres
        self.last_name = last_name  # Nom de famille

    def born(self, **kwargs):
        """Ajoute un enfant à la liste des membres et imprime un message de félicitations."""
        self.members.append(kwargs)  # Ajoute un dictionnaire avec les détails de l'enfant
        print(f"Congratulations, the {self.last_name} family has a new member!")

    def is_18(self, name):
        """Retourne True si l'âge du membre est supérieur ou égal à 18, sinon False."""
        for member in self.members:
            if member['name'] == name:
                return member['age'] >= 18
        return False  # Si le membre n'est pas trouvé, on retourne False

    def family_presentation(self):
        """Affiche les détails de la famille et de ses membres."""
        print(f"The {self.last_name} Family:")
        for member in self.members:
            print(f"{member['name']} - Age: {member['age']}, Gender: {member['gender']}, Child: {member['is_child']}")

family = Family("Smith")

# Ajout des membres
family.born(name="Michael", age=35, gender="Male", is_child=False)
family.born(name="Sarah", age=32, gender="Female", is_child=False)

# Appel des méthodes
print(f"Is Michael over 18? {family.is_18('Michael')}")
print(f"Is Sarah over 18? {family.is_18('Sarah')}")
family.family_presentation()
print(family.members)

