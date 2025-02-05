import random
def get_random_temp():
    random_number=random.randint(-10,40)
    return random_number
print(get_random_temp())

def main():
    temperature=get_random_temp()
    print(f"The temperature right now is {temperature} degrees Celsius.")
main()
def main():
    temperature=get_random_temp()
    print(f"The temperature right now is {temperature} degrees Celsius.")
    if temperature<0:
        print("thats freezing! Wear some extra layers today")
    elif 0<=temperature<=16:
      print("Quite chilly! Don’t forget your coat")
    else:
      print("The temperature is good")
main()
def get_random_temp(season):
   if season == "winter":
        return random.randint(-10, 16)
   elif season == "spring":
        return random.randint(5, 22)
    
print(get_random_temp("winter"))

def main():
    use_season=input("Enter a season")
    temperature=get_random_temp(use_season)
main()
      
      
