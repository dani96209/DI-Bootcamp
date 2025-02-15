# Part 1: Quizz
# What is a class? # A blueprint for creating objects, defining properties (attributes) and behaviors (methods).
# What is an instance? # A specific object created from a class
# What is encapsulation? # The concept of hiding the internal details of an object and exposing only the necessary functionality
# What is abstraction? # Simplifying complex systems by providing a high-level interface while hiding the implementation details
# What is inheritance? # A mechanism where a class inherits attributes and methods from another class.
# What is multiple inheritance? # A feature where a class can inherit from more than one base class.
# What is polymorphism? #The ability of different objects to respond to the same method in different ways
# What is method resolution order or MRO? # The order in which Python searches for a method in the class hierarchy. It defines the order in which base classes are called in case of multiple inheritance.


import random

class Card:
    def __init__(self, suit, value):
        """Initializes a card with a suit and a value."""

        self.suit = suit
        self.value = value

    def __repr__(self):
        """Textual representation of a card."""
        return f"{self.value} of {self.suit}"

class Deck:
    def __init__(self):
        """Initializes a 52-card deck."""

        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        self.cards = [Card(suit, value) for suit in suits for value in values]
        self.shuffle()  # Auto mix at start


    def shuffle(self):
        """Shuffle the deck of cards."""
        if len(self.cards) == 52:  # Check that we have a complete deck

            random.shuffle(self.cards)
        else:
            print("The deck is not complete, cannot be shuffled!")
 

    def deal(self):
        """Deals a card from the deck."""

        return self.cards.pop() if self.cards else None  # Returns None if the deck is empty


# === Cards Game Testview===
deck = Deck()  
print(deck.deal())  # Draw a card

print(deck.deal())  # Draw another card
print(len(deck.cards))  # Shows the number of cards remaining


print(deck.cards)
print(deck.deal())
print(len(deck.cards))


