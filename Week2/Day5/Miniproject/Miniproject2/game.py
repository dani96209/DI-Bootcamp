import random
class Game():
    def get_user_item(self):
        valid_items = ['rock', 'paper', 'scissors']
        while True:
          users_item=input("Select an item (rock/paper/scissors)")
          if users_item in valid_items:
                return users_item  # Return the valid choice
          else:
                print("Invalid input. Please choose either 'rock', 'paper', or 'scissors'.")
          return users_item
        
    def get_computer_item(self):
        valid_items = ['rock', 'paper', 'scissors']
        computers_choice=random.choice(valid_items)
        return computers_choice
    def get_game_result(self, user_item, computer_item):
        
        if user_item == computer_item:
            return "draw"  # If both choices are the same
        elif (user_item == 'rock' and computer_item == 'scissors') or \
             (user_item == 'paper' and computer_item == 'rock') or \
             (user_item == 'scissors' and computer_item == 'paper'):
            return "win"  # If the user wins
        else:
            return "loss"  
        
    def play(self):
        # Get the user's choice
        user_item = self.get_user_item()
        
        # Get the computer's choice
        computer_item = self.get_computer_item()
        
        # Determine the result of the game
        result = self.get_game_result(user_item, computer_item)
        
        # Print the output of the game
        if result == "win":
            print(f"You selected {user_item}. The computer selected {computer_item}. You win!")
        elif result == "draw":
            print(f"You selected {user_item}. The computer selected {computer_item}. You drew!")
        else:
            print(f"You selected {user_item}. The computer selected {computer_item}. You lose!")
        
        # Return the result
        return result
