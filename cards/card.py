class Card:
    """
    A class to represent a single poker-style card.

    Attributes
    ----------
    suit : suit.Suit
        The suit (enum) of the card: hearts, spades, clubs, diamonds
    rank : rank.Rank
        The rank (enum) of the card. Can be one of the following:
        Ace, 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King
    name : str
        The name of the card: '[RANK] of [SUIT]'
    """
    def __init__(self, suit, rank):
        """
        Constructor.

        Parameters
        ----------
        suit : suit.Suit
            The suit (enum) of the card.
        rank : rank.Rank
            The rank (enum) of the card.
        """
        self.suit = suit
        self.rank = rank
        self.name = f'{self.rank.name} of {self.suit.name}'
