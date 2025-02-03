fav_fruits=input("What's your favorite fruits?")
list_fruits=fav_fruits.split()
print(list_fruits)
fav_fruits_user=input("Put a fruit's name")
if fav_fruits_user in list_fruits:
    print("You choose one of your favorite fruits!Enjoy!")
else:
    print("You chose a new fruit. I hope you enjoy")