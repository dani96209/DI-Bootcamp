import string

def clean_text(text):
    """Nettoie le texte en supprimant la ponctuation et en mettant en minuscules."""
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))  # Supprime la ponctuation
    return text.split()  # Sépare en mots

class Text:
    def __init__(self, text):
        self.text = text
        self.words = clean_text(text)  # Nettoyage des mots

    @classmethod
    def from_file(cls, filename, encoding='utf-8'):
        """Crée une instance de Text à partir d'un fichier"""
        try:
            with open(filename, 'r', encoding=encoding, errors="ignore") as file:
                text = file.read()
            return cls(text)
        except FileNotFoundError:
            print(f"Le fichier '{filename}' n'a pas été trouvé.")
            return None
        except Exception as e:
            print(f"Une erreur s'est produite : {e}")
            return None

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
        word_count = {}
        for word in self.words:
            word_count[word] = word_count.get(word, 0) + 1  # Version simplifiée

        return max(word_count, key=word_count.get) if word_count else None

    def unique_words(self):
        """Retourne une liste de tous les mots uniques"""
        word_count = {}
        for word in self.words:
            word_count[word] = word_count.get(word, 0) + 1

        return [word for word, count in word_count.items() if count == 1]

# Test avec un fichier
text_instance = Text.from_file('C:\\Users\\daniel\\Documents\\the_stranger.txt')

if text_instance:
    print(text_instance.word_frequency('partial'))  # Vérifier la fréquence du mot "partial"
    print(text_instance.most_common_word())         # Trouver le mot le plus fréquent
    print(text_instance.unique_words())          