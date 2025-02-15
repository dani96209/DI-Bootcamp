from game import Game
def get_user_menu_choice():
    """
    Display a simple menu and get the user's choice with data validation.
    Possible choices: Play a new game, Show scores, or Quit.
    """
    menu_options = ["Play a new game", "Show scores", "Quit"]
    print("Please choose an option:")
    for i, option in enumerate(menu_options, start=1):
        print(f"{i}. {option}")

    while True:
        try:
            choice = int(input("Enter the number of your choice: "))
            if choice < 1 or choice > 3:
                raise ValueError("Invalid choice. Please choose a valid option.")
            return menu_options[choice - 1]
        except ValueError as e:
            print(e)

def print_results(results):
    """
    Print the results of the games played in a user-friendly way.
    It takes a dictionary with keys 'win', 'loss', and 'draw'.
    """
    print("\nGame Results:")
    print(f"Wins: {results.get('win', 0)}")
    print(f"Losses: {results.get('loss', 0)}")
    print(f"Draws: {results.get('draw', 0)}")
    print("\nThank you for playing!")

def main():
    """
    Main function that controls the game loop.
    - Displays menu options.
    - Plays games when selected.
    - Shows scores or exits when chosen.
    """
    results = {"win": 0, "loss": 0, "draw": 0}  # Track game outcomes

    while True:
        choice = get_user_menu_choice()

        if choice == "Play a new game":
            game = Game()  # Create a new game instance
            result = game.play()  # Play the game and get the result
            results[result] += 1  # Update results dictionary

        elif choice == "Show scores":
            print_results(results)  # Show results so far

        elif choice == "Quit":
            print_results(results)  # Print final summary before exiting
            print("Goodbye!")
            break  # Exit the game loop

# Run the main function if the script is executed directly
if __name__ == "__main__":
    main()