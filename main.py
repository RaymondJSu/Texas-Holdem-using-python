class Card(object):
    def __init__(self, name, value, suit):
        self.value = value
        self.suit = suit
        self.name = name

    def __repr__(self):
        return str(self.name) + ' of ' + self.suit


class StandardDeck(list):
    def __init__(self):
        suits = ['Hearts', 'Spades', 'Diamonds', 'Clubs']
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
                self.append(Card(name, values[name], suit))
