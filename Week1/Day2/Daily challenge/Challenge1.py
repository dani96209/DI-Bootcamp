user_number=int(input("Enter a number"))
user_length=int(input("Enter a length"))
multiples = [user_number * i for i in range(1, user_length+1)]
print(multiples)