#Utilisation de pip install faker à partir du terminal
from faker import Faker

# Créer une instance de Faker
fake = Faker()

# Créer une liste vide pour stocker les utilisateurs
users = []

def ajouter_utilisateur():
    # Créer un dictionnaire d'utilisateur avec des données fictives
    utilisateur = {
        'name': fake.name(),
        'address': fake.address(),
        'language_code': fake.language_code()
    }
    
    # Ajouter l'utilisateur à la liste des utilisateurs
    users.append(utilisateur)

# Exemple d'ajout de 5 utilisateurs fictifs
for _ in range(5):
    ajouter_utilisateur()

# Afficher la liste des utilisateurs
for utilisateur in users:
    print(utilisateur)