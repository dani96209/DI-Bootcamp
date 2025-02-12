import datetime

def minutes_vécues(date_naissance):
    # Convertir la chaîne de la date de naissance en objet datetime
    date_naissance = datetime.datetime.strptime(date_naissance, "%Y-%m-%d")
    
    # Obtenir la date actuelle
    maintenant = datetime.datetime.now()
    
    # Calculer la différence entre la date actuelle et la date de naissance
    difference = maintenant - date_naissance
    
    # Convertir la différence en minutes
    minutes_vécues = difference.total_seconds() / 60
    
    # Afficher le message
    print(f"Vous avez vécu {minutes_vécues:.0f} minutes jusqu'à aujourd'hui.")

# Exemple d'appel de la fonction
minutes_vécues("1990-06-15")  # Remplacer par la date de naissance souhaitée