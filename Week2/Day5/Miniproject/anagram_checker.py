class AnagramChecker():
    def __init__(self, word_list_file="C:\\Users\\daniel\\Documents\\sowpods.txt"):
        """Loads the word list from the given file into a set for quick lookup."""
        try:
            with open(word_list_file, 'r', encoding='utf-8') as file:
                self.word_list = set(word.strip().lower() for word in file.readlines())
        except FileNotFoundError:
            print(f"Error: The file '{word_list_file}' was not found.")
            self.word_list = set()

    def is_valid_word(self, word):
        """Checks if a given word is valid (exists in the word list)."""
        return word.lower() in self.word_list
    def get_anagrams(self, word):
        """Finds all anagrams of the given word in the word list."""
        sorted_word = sorted(word.lower())
        return [w for w in self.word_list if sorted(w) == sorted_word and w != word.lower()]

    