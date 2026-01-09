# Part 1 : Quizz :
# Answer the following questions

# What is a class?
# Answer: In Python, a class is a blueprint or template for creating objects. It defines the structure (attributes) and behavior (methods) that all objects created from that class will share, but each object (instance) maintains its own unique set of data. 

# What is an instance?
# Answer: A single, unique realization of a class. Each instance has its own unique set of data (instance variables), which are distinct from the data in other instances of the same class.

# What is encapsulation?
# Answer: Encapsulation in OOP bundles data (attributes) and the methods that operate on that data into a single unit (a class) and restricts direct access to the internal state, protecting it from outside interference, allowing changes only through defined methods (getters/setters)

# What is abstraction?
# Answer: Abstraction in Python is a core principle of OOP that involves hiding unnecessary implementation details and showing only the essential features or functionalities to the user. It simplifies complex systems by allowing developers to focus on what an object *does* rather than *how* it does it. 

# What is inheritance?
# Answer: Inheritance in OOP is a mechanism where a new class (child/derived) acquires properties (attributes) and behaviors (methods) from an existing class (parent/base), promoting code reuse, creating a logical class hierarchy, and making code more modular and maintainable by defining common features in one place

# What is multiple inheritance?
# Answer: Multiple inheritance in OOP is a feature allowing a single class (child) to inherit properties and methods from *more* than one parent class, combining functionalities from different sources.

# What is polymorphism?
# Answer: Polymorphism in OOP means "many forms," allowing a single interface (like a method name) to represent different underlying data types or classes, enabling objects of different types to be treated similarly but respond uniquely

# What is method resolution order or MRO?
# Answer: Method Resolution Order is the sequence in which Python searches for attributes (methods and variables) within a class hierarchy. This process is crucial in Python's object-oriented programming model, especially when a class inherits from multiple parent classes, allowing Python to resolve potential naming conflicts predictably. 

# Part 2: Create a deck of cards class.
# The Deck of cards class should NOT inherit from a Card class.

# The requirements are as follows:
# The Card class should have a suit (Hearts, Diamonds, Clubs, Spades) and a value (A,2,3,4,5,6,7,8,9,10,J,Q,K)
# The Deck class :
# should have a shuffle method which makes sure the deck of cards has all 52 cards and then rearranges them randomly.
# should have a method called deal which deals a single card from the deck. After a card is dealt, it should be removed from the deck.
from random import shuffle
import sys
from time import sleep

SUITS = ["Hearts", "Diamonds", "Clubs", "Spades"]
VALUES = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]

class Card:
    def __init__(self, suit: str, value: str):
        self.suit = suit
        self.value = value

class Deck:
    def __init__(self):
        self.cards = [Card(suit, value) for suit in SUITS for value in VALUES]

    def __repr__(self):
        deck = str()
        for card in self.cards:
            deck += f"{card.value} of {card.suit}\n"
        return deck

    def shuffle(self) -> None:
        """
        shuffles the deck of cards, if it is complete
        
        """
        if len(self.cards) == 52:
            shuffle(self.cards)
        else:
            print("The deck is incomplete.")
    
    def deal(self) -> Card:
        """
        deals a card from the deck if the deck is not empty
        
        :return: the card that was dealt
        :rtype: Card
        """
        if self.cards == []:
            print("The deck is empty.")
        else:
            print("Dealing card", end="")
            for char in "...":
                sys.stdout.write(char)
                sys.stdout.flush() 
                sleep(0.5)
            print()
            card_dealt = self.cards.pop()
            print(f"Card dealt: {card_dealt.value} of {card_dealt.suit}.")
            return card_dealt

def play():
    deck1 = Deck()
    print('Before shuffle: ')
    print()
    print(deck1)
    print('After shuffle: ')
    print()
    deck1.shuffle()
    print(deck1)

    card_dealt = deck1.deal()
    print(f"The card {card_dealt.value} of {card_dealt.suit} is in the deck: {card_dealt in deck1.cards}")

play()


