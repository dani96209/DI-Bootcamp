for i in range(1,21):
    print(i)
    
new_list=list(range(1,21))
print(new_list)

for i, element in enumerate(new_list):
    if i%2==0:
        print(new_list[i])
    