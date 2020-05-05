"""Play Cards with a deck"""


from deck import Deck

myDeck = Deck()
myDeck.show()

myHand = Deck("hand")
myHand.show()

myDeck.shuffle()
myDeck.show()
