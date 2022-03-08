#!/usr/bin/python
import random
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + ' of ' + self.suit  # A of Hearts for example


class Deck:
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                currentCard = (Card(suit, rank))
                self.deck.append(currentCard)
                
    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n' + card.__str__() # the Card class's __str__ method
        return 'The deck contains' + deck_comp

    def shuffle(self):
        random.shuffle(self.deck)
    
    def deal(self):
        single_card = self.deck.pop()
        return single_card

class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)


# if this script is being run as terminal command; run what's under this. If you didn't have that, I assume this is a module/library. Not treating like a script.
if __name__ == '__main__':
    cardy = Card("heart", "Ace")
    # print(cardy)

    decky = Deck()
    # print(decky) # prints whole deck
    # print(decky.deck.pop()) # last one

    print("dealing card")
    decky.shuffle()
    print(decky.deal())