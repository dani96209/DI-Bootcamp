class Text:
    def __init__(self, text):
        # On transforme le texte en une liste de mots en minuscules
        self.text = text
        self.words = self.text.lower().split()

    def word_frequency(self, word):
        """Retourne la fréquence d'un mot dans le texte"""
        if not word:
            return None
        word_count = self.words.count(word.lower())
        if word_count == 0:
            return f"The word '{word}' is not in the text."
        return word_count

    def most_common_word(self):
        """Retourne le mot le plus fréquent dans le texte"""
        # Créer un dictionnaire pour compter les occurrences des mots
        word_count = {}
        for word in self.words:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1
        
        # Trouver le mot le plus fréquent
        most_common_word = None
        highest_frequency = 0
        for word, frequency in word_count.items():
            if frequency > highest_frequency:
                most_common_word = word
                highest_frequency = frequency
        
        return most_common_word

    def unique_words(self):
       word_count = {}
       for word in self.words:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1
        # Filtrer les mots qui apparaissent une seule fois
       unique_words = [word for word, count in word_count.items() if count == 1]
       return unique_words

# Exemple d'utilisation avec un texte simple
text = "A  good book would sometimes cost as much as a good house."
text_instance = Text(text)

# Test des méthodes
print(text_instance.word_frequency('good'))  # Affiche la fréquence du mot "good"
print(text_instance.most_common_word())      # Affiche le mot le plus fréquent
print(text_instance.unique_words())          # Affiche les mots uniques