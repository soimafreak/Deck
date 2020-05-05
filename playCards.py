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

print("now add an 8th card to hand and watch for an error")
try:
    myHand.return_card(myDeck.deal_card())
except Exception as e:
    myDeck.return_card(e[1])
    print("Failed to add card to myHand with error: {}".format(e[0]))


print("myDeck has {} cards".format(len(myDeck.cards)))
print("myHand has {} cards".format(len(myHand.cards)))
print("Return the hand to the Deck")
deckCount = len(myHand.cards)
i=1;
while i <= deckCount:
    i += 1
    myDeck.return_card(myHand.deal_card())
    myHand.show()

print("myDeck has {} cards".format(len(myDeck.cards)))
print("myHand has {} cards".format(len(myHand.cards)))
myHand.show()
