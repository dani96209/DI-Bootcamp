#Challenge 1
words_sequence = "without,hello,bag,world"
words_list = words_sequence.split(",")  # 
print(words_list)
sorted_list=sorted(words_list)
print(sorted_list)
sorted_words=",".join(sorted_list)
print(words_sequence)
print(sorted_words)

#Challenge 2
def longest_word(sentence):
    liste=sentence.split(" ")
    strong_word=max(liste,key=len)
    print(strong_word)

longest_word("A thing of beauty is a joy forever")
longest_word("Forgetfulness is by all means powerless!")
longest_word("Margaret's toy is a pretty doll.")
    
