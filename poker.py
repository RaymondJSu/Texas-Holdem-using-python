import random
from xml.dom.expatbuilder import theDOMImplementation

class Card(object):
    def __init__(self, name, value, suit):
        self.value = value
        self.suit = suit
        self.name = name
        self.showing = False

    def __repr__(self):
        if self.showing:
            return str(self.name) + ' of ' + self.suit
        else:
            return 'Card'

class Deck(object):
    def shuffle(self, times = 1):
        random.shuffle(self.cards)
        print('Deck Shuffled')

    def deal(self):
        return self.cards.pop(0)

class StandardDeck(Deck):
    def __init__(self):
        self.cards = []
        suits = {"Hearts":"♡", "Spades":"♠", "Diamonds":"♢", "Clubs":"♣"}
        values = {'Two': 2,
                  'Three': 3,
                  'Four': 4,
                  'Five': 5,
                  'Six': 6,
                  'Seven': 7,
                  'Eight': 8,
                  'Nine': 9,
                  'Ten': 10,
                  'Jack': 11,
                  'Queen': 12,
                  'King': 13,
                  'Ace': 14}
        for name in values:
            for suit in suits:
                self.cards.append(Card(name, values[name], suit))

    def ___repr__(self):
        return 'Standard deck of cards: {0} remaining'.format(len(self.cards))
    
class Player(object):
    def __init__(self):
        self.cards = []

    def cardCount(self):
        return len(self.cards)

    def addCard(self, card):
        self.cards.append(card)

class PokerScorer(object):
    def __init___(self, cards):
        # Number of cards
        if not len(cards) == 5:
            return 'Error: Wrong number of cards'
        self.cards = cards

    def suitCount(self):
        suits = [card.suit for card in self.cards]
        return list(set(suits))

    def is_flush(self):
        suits = [card.suit for card in self.cards]
        if len(set(suits)) == 1:
            return True
        return False

    def is_straight(self):
        values = [card.value for card in self.cards]
        values.sort()

        if not len(set(values)) == 5:
            return False 

        if values[4] == 14 and values[3] == 5 and values[2] == 4 and values[1] == 3 and values[0] == 2:
            return 5  
        else:
            if not values[0] + 1 == values[1]: return False
            if not values[1] + 1 == values[2]: return False
            if not values[2] + 1 == values[3]: return False
            if not values[3] + 1 == values[4]: return False
        
        return values[4]

    def is_highcard(self):
        values = [card.value for card in self.cards]
        highcard = None
        for card in self.cards:
            if highcard is None:
                highcard = card
            elif highcard.value < card.value:
                highcard = card

    def is_pairs(self):
        pairs = []
        values = [card.value for card in self.cards]
        for value in values:
            if values.count(value) == 2 and value not in pairs:
                pairs.append(value)
        return pairs
    
    def is_fourkind(self):
        values = [card.value for card in self.cards]
        for value in values:
            if values.count(value) == 4:
                return True

    def is_fullHouse(self):
        two = False
        three = False
        
        values = [card.value for card in self.cards]
        if values.count(values) == 2:
            two = True
        elif values.count(values) == 3:
            three = True
        
        if two and three:
            return True
            
        return False

    def is_threes(self):
        pass
        
def main():
    deck = StandardDeck()
    cody = Player()
    deck.shuffle()
    for i in range(5):
        cody.cards.append(deck.deal())
    print(cody.cards)
    for i in range(5):
        cody.cards[i].showing = True
    print(cody.cards)
    


if __name__ == '__main__':
    main()
