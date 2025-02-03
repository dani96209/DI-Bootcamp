sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]

while "Pastrami sandwich" in sandwich_orders:
    sandwich_orders.remove("Pastrami sandwich")
finished_sandwiches = []
while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)  
    print(f"Making your {current_sandwich}...")
    finished_sandwiches.append(current_sandwich)
print("\nAll sandwiches have been made:")
for sandwich in finished_sandwiches:
    print(f"I made your  {sandwich}")