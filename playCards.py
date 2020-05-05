"""Play Cards with a deck"""


from deck import Deck

print("Create a deck and a hand")
myDeck = Deck()
myDeck.show()
myHand = Deck("hand")
myHand.show()

print("Shuffle the deck")
myDeck.shuffle()
myDeck.show()

print("Check the Hand is empty and the Deck is full")
print("myDeck has {} cards".format(len(myDeck.cards)))
print("myHand has {} cards".format(len(myHand.cards)))

print("Deal 7 cards to the hand")
for i in range(0,7):
    myHand.return_card(myDeck.deal_card())

print("myDeck has {} cards".format(len(myDeck.cards)))
myDeck.show()
print("myHand has {} cards".format(len(myHand.cards)))
myHand.show()
