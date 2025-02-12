import random
import string

# Générer une chaîne aléatoire de longueur 5 avec uniquement des lettres majuscules et minuscules
random_string = ''.join(random.choices(string.ascii_letters, k=5))
print(random_string)