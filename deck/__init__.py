"""Deck Class.

This is where Decks are defined.
"""

from . import exceptions
from card import Card
import random

class Deck(object):
    """Deck Class."""

    def __init__(self, deck_type='pack'):
        """Init the Deck.

        this should either be as a full deck of cards or as an empty deck."""

        self.cards = []

        if deck_type == "pack":
            for s in ['spades', 'diamonds', 'clubs', 'hearts']:
                for n in range(1,14):
                    self.cards.append(Card(s,n))
        if deck_type not in ("pack, hand"):
            raise exceptions.NotADeck

    def shuffle(self):
        for i in range(len(self.cards) - 1, 0, -1):
            rand = random.randint(0, i)
            self.cards[i], self.cards[rand] = self.cards[rand], self.cards[i]


    def deal_card(self, position='top'):
        if position == 'top':
            return self.cards.pop(0)
        elif position == 'bottom':
            return self.cards.pop()
        else:
            pos = random.randint(0, len(self.cards))
            return self.cards.pop(pos)

    def return_card(self, card, position='top'):
        if position == 'top':
            self.cards.insert(0,card)
        elif position == 'bottom':
            self.cards.append(card)
        else:
            pos = random.randint(0, len(self.cards))
            self.cards.insert(pos, card)

    def show(self):
        if len(self.cards) > 0:
            for i in self.cards:
                if i.number > 1 and i.number <= 10:
                    print("{} of {}".format(i.number, i.suite))
                else:
                    print("{} of {}".format(i.face, i.suite))
        else:
            print("No cards in Deck")
