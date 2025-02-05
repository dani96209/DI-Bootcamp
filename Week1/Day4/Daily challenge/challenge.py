matrix = [
    "7ii",
    "Tsx",
    "h%?",
    "i #",
    "sM ",
    "$a ",
    "#t%",
    "^r!"
]


matrix_decrypted = []


for col in range(len(matrix[0])):  
    for row in matrix:
        if col < len(row):  
            matrix_decrypted.append(row[col])  


matrix_decrypted = ''.join(matrix_decrypted)


matrix_decrypted = matrix_decrypted.replace('%', ' ').replace('?', ' ').replace('$', ' ').replace('7',' ').replace('#',' ').replace('!',' ').replace('^',' ')


matrix_decrypted = ' '.join(matrix_decrypted.split())


print(matrix_decrypted)