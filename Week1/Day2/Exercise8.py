toppings_pizza=[]
toppings_numbers=0
Guess_topic_pizza=input("Enter a pizza topping")
while Guess_topic_pizza!="quit":
    Guess_topic_pizza=input("Enter a pizza topping")
    toppings_pizza.append(Guess_topic_pizza)
    toppings_numbers+=1
    print("added this topping in your pizza")

print(toppings_pizza,"The total price is",10+2.5*toppings_numbers)