from random import randint


class Card:
    def __init__(self, suit, value) -> None:
        self.suit = suit
        self.value = value

    def print_card(self):
        if self.value == 'J':
            print('Jack of {}'.format(self.suit))
        elif self.value == 'Q':
            print('Queen of {}'.format(self.suit))
        elif self.value == 'K':
            print('King of {}'.format(self.suit))
        else:
            print('{} of {}'.format(self.value, self.suit))


class Deck:
    def __init__(self) -> None:
        self.cards = []
        for suit in ['Clubs', 'Hearts', 'Diamonds', 'Spades']:
            for value in ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']:
                newCard = Card(suit, value)
                self.cards.append(newCard)

    def print_deck(self):
        for card in self.cards:
            card.print_card()

    def shuffle(self):
        shuffled_deck = []
        while len(self.cards) > 0:
            pos = randint(0, len(self.cards)-1)
            shuffled_deck.append(self.cards.pop(pos))
        self.cards = shuffled_deck


myDeck = Deck()
print('\nStarting deck --------------------')
myDeck.print_deck()
print('\nReshuffled deck ------------------')
myDeck.shuffle()
myDeck.print_deck()
print('----------------------------------')
