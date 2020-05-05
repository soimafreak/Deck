"""Card Class.

Define A Card so that a Deck can be made up of many cards."""

from . import exceptions

class Card(object):
    """Card Class.

    A card has a some properties:
    Suite: Hearts, Diamonds, Spades, Clubs
    Value: 1-11 *NB* This can be 2 values as with an Ace [1 or 11]
    Number: 1-13
    Face: King, Queen, jack
    """
    def __init__(self, suite, number):

        if suite.lower() in ['hearts','diamonds','spades', 'clubs']:
            self.suite = suite
        else:
            raise exception.NotASuite
        if number >= 0 and number <= 13:
            self.number = number
        else:
            raise exception.NumberOutsideOfRange
        if number > 10:
            self.value = [10]
        elif number == 1:
            self.value = [1,11]
        else:
            self.value = [number]

        if number > 10:
            if number == 11:
                self.face = "Jack"
            elif number == 12:
                self.face = "Queen"
            elif number == 13:
                self.face = "King"
        elif number == 1:
            self.face = "Ace"
        else:
            self.face = False
