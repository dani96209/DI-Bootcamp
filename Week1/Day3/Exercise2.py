family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
total_cost=0
for i,v in family.items():
    if v<3:
        print(f"{i} will pay nothing")
        total_cost+=0
    elif v>3 and v<12:
        print(f"For {i}, the ticket price is 10$")
        total_cost+=10
    elif v>15:
        print(f"For {i},the ticket price is 15$")
        total_cost+=15
print(f"The total cost is {total_cost} ")

family = {}
num_members = int(input("How much family member would you want entry ? "))
for _ in range(num_members):
    name = input("Entrez le nom : ")
    age = int(input(f"Entrez l'âge de {name} : "))
    family[name] = age  
print(family)