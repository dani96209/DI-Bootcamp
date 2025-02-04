user_word = input("Enter a word: ")

letter_dict = {}

for index, letter in enumerate(user_word):
    if letter not in letter_dict:
        letter_dict[letter] = []  
    letter_dict[letter].append(index)  

print(letter_dict)