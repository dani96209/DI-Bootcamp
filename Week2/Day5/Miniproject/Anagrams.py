from anagram_checker import AnagramChecker

def get_user_word():
    """Gets a valid single word input from the user."""
    while True:
        user_input = input("Enter a word (or type 'exit' to quit): ").strip()
        if user_input.lower() == 'exit':
            return None
        if not user_input.isalpha():
            print("Error: Please enter only alphabetic characters.")
            continue
        if ' ' in user_input:
            print("Error: Please enter a single word without spaces.")
            continue
        return user_input

def main():
    """Runs the main program loop."""
    checker = AnagramChecker("C:\\Users\\daniel\\Documents\\sowpods.txt")  # Make sure the file exists

    print("Welcome to the Anagram Checker!")
    
    while True:
        word = get_user_word()
        if word is None:
            print("Goodbye!")
            break
        
        if not checker.is_valid_word(word):
            print(f"Sorry, '{word}' is not a valid English word.")
            continue

        anagrams = checker.get_anagrams(word)
        print(f"\nYOUR WORD: \"{word.upper()}\"")
        print("This is a valid English word.")
        print(f"Anagrams for your word: {', '.join(anagrams) if anagrams else 'None found'}\n")

if __name__ == "__main__":
    main()