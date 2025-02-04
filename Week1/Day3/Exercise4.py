users = ["Mickey","Minnie","Donald","Ariel","Pluto"]
disney_users_A = {}
for index, user in enumerate(users):
    disney_users_A[user] = index

print(disney_users_A)

disney_users_B = {}
for index, user in enumerate(users):
    disney_users_B[index] = user

print(disney_users_B)

users_2=["Ariel","Donald","Mickey","Minnie","Pluto"]
disney_users_C={}
for index, user_2 in enumerate(users_2):
    disney_users_C[user_2] = index

print(disney_users_C)

disney_users_A = {user: index for index, user in enumerate(users) if 'i' in user}
print(disney_users_A)
disney_users_A = {index: user for index, user in enumerate(users) if user[0].lower() in ['m', 'p']}
print(disney_users_A)
