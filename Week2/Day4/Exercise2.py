import json

# JSON de départ
sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

# Charger le JSON dans un dictionnaire Python
data = json.loads(sampleJson)
print(data)
# Accéder à la clé "salary"
salary = data["company"]["employee"]["payable"]["salary"]
print(f"Salary: {salary}")

# Ajouter la clé "birth_date" au même niveau que "name"
data["company"]["employee"]["birth_date"] = "1990-05-01"

# Sauvegarder le dictionnaire modifié dans un fichier JSON
with open("employee_data.json", "w") as json_file:
    json.dump(data, json_file, indent=4)

# Afficher les données modifiées
print("\nModified JSON data:")
print(json.dumps(data, indent=4))