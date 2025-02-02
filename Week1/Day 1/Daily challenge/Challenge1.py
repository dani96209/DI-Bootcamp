user_string=input("Enter a string")
if len(user_string)<10:
    print("string not long enough")
elif len(user_string)>10:
    print("string too long")
elif len(user_string)==10:
    print("perfect string")

for i in range(1, len(user_string) + 1):
    print(user_string[:i])

import random
my_list=list(user_string)
print(my_list)
random.shuffle(my_list)
mixed_string=''.join(my_list)
print(mixed_string)

