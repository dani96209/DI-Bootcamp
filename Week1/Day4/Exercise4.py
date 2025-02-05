import random
def guess_the_number(number):
    good_number=random.randint(1,100)
    if number==good_number:
        print("You succeed")
    else :
        print("You failed")
    return good_number,number
print(guess_the_number(23))
