class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit


class Deck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    pos = -1

    def __init__(self):
        self.cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __iter__(self):
        return self

    def __next__(self):
        if self.pos < len(self.cards)-1:
            self.pos += 1
            return f'{self.cards[self.pos].rank} {self.cards[self.pos].suit}'
        else:
            raise StopIteration


deck = Deck()
for card in deck:
    print(card)
