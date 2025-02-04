brand=zara_info = {
    "name": "Zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": ["men", "women", "children", "home"],
    "international_competitors": ["Gap", "H&M", "Benetton"],
    "number_stores": 7000,
    "major_color": {
        "France": "blue",
        "Spain": "red",
        "US": ["pink", "green"]
    }
}

print(brand)
brand["number_stores"]=2
print(brand)
clients = ", ".join(brand["type_of_clothes"]) 
print(f"Zara's clients include {clients}.")
brand["country_creation"]="Spain"
print(brand)

if "international_competitors" in brand:
    brand["international_competitors"].append("Desigual")  
print(brand)
del brand["creation_date"]
print(brand)
print(brand["international_competitors"][-1])
print(brand["major_color"]["US"])
print(len(brand.items()))
print(brand.keys())
more_on_zara={"creation_date": 1975, 
"number_stores": 10000}
print(more_on_zara)
brand.update(more_on_zara)
print(brand)
print(brand["number_stores"])