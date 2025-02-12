import datetime

def afficher_date_actuelle():
    # Obtenir la date actuelle
    date_actuelle = datetime.date.today()
    print("La date actuelle est :", date_actuelle)

# Appeler la fonction pour afficher la date
afficher_date_actuelle()