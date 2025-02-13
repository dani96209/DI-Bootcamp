import os
import random
print(os.getcwd())
list_words=[]
def get_words_from_file():
    with open("C:\\Users\\daniel\\Documents\\DI-Bootcamp\\Week2\\Day4\\words.txt","r",encoding="utf-8") as f:
       read_words= f.readlines()
       for word in read_words:  # Afficher chaque mot
            list_words.append(word.strip())
            

def get_random_sentence(length):

    
    random_sentence=' '.join(random.choice(list_words)for _ in range(length))
    return random_sentence.lower()

def main():
    """Fonction principale qui gère l'entrée de l'utilisateur et génère une phrase"""
    print("Ce programme génère une phrase aléatoire à partir d'un fichier de mots.")
    
    # Demander à l'utilisateur la longueur de la phrase
    try:
        length = int(input("Combien de mots voulez-vous dans la phrase ? (entre 2 et 20): "))
        
        # Validation de l'entrée
        if length < 2 or length > 20:
            print("Erreur : Le nombre de mots doit être entre 2 et 20.")
            return  # Arrêter le programme si la valeur est incorrecte
        
    except ValueError:
        print("Erreur : Veuillez entrer un nombre entier.")
        return  # Arrêter le programme si l'entrée n'est pas un entier
    
    # Charger les mots depuis le fichier
    get_words_from_file()

    # Générer et afficher la phrase
    random_sentence = get_random_sentence(length)
    print("Voici la phrase générée :")
    print(random_sentence)


            
main()



