fmly_number1_age=int(input("What's your age?"))
fmly_number2_age=int(input("What's your age?"))
total_cost=0
if fmly_number1_age<3 and fmly_number2_age<3:
    price=0
    print("The tickets is free")
elif fmly_number1_age <=12 and fmly_number2_age<=12:
    price=10
    print("The ticket is 10$")
elif fmly_number1_age>12 and fmly_number2_age>12:
    price=15
    print("The ticket is 15$")
total_cost+=price
print("The total price is",total_cost)

teenagers_group=["Linda","Jacob","Daniel"]
for teenager in teenagers_group:
    teenager_age=int(input("What's your age?"))
    if teenager_age<16:
        teenagers_group.remove(teenager)
print(teenagers_group)

