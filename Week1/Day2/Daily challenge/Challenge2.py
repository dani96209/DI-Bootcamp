users_word = input("Enter a word: ")
result = list()


for char in users_word:
    if char not in result:  
        result.append(char)

new_word = "".join(result)

print( new_word)
            
