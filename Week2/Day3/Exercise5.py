import datetime

def temps_restants_jusqu_a_janvier():
    # Obtenir la date actuelle
    maintenant = datetime.datetime.now()
    
    # Créer un objet datetime pour le 1er janvier de l'année suivante
    an_prochain = maintenant.year + 1
    janvier_1 = datetime.datetime(an_prochain, 1, 1)
    
    # Calculer la différence entre le 1er janvier et la date actuelle
    temps_restant = janvier_1 - maintenant
    
    # Afficher le temps restant
    jours = temps_restant.days
    heures, reste = divmod(temps_restant.seconds, 3600)
    minutes, secondes = divmod(reste, 60)
    
    print(f"Il reste {jours} jours, {heures} heures, {minutes} minutes et {secondes} secondes jusqu'au 1er janvier.")

# Appeler la fonction pour afficher le temps restant
temps_restants_jusqu_a_janvier()