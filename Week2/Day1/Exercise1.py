class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

cat_1=Cat("Theodor",10)
cat_2=Cat("Buck",8)
cat_3=Cat("Mickey",7)
old_age_list=[]
print(cat_1.age)


def oldest_cat():
    """Retourne le nom et l'âge du chat le plus âgé."""
    old_age_list = [cat_1, cat_2, cat_3]  # List Cat objects
    oldest = max(old_age_list, key=lambda cat: cat.age)  # Finding the cat with age  max
    return oldest.name, oldest.age  # Return name and age

# Retrieving of informations  on the oldest cat
cat_name, cat_age = oldest_cat()

# Showing  of exact sentence asked
print(f"The oldest cat is {cat_name}, and is {cat_age} years old.")

