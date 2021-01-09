import random

from .card import Card
from .rank import Rank
from .suit import Suit

class Deck:
    """
    A class to represent a deck of 52 poker-style playing cards.
    """
    def __init__(self, seed=42):
        """
        Constructor.

        Attributes
        ----------
        seed : int
            The seed used to initialize pseudorandomness.
        """
        random.seed(seed)

        # initialize deck of cards in order
        self.reset()

    def shuffle(self, reset=False):
        """
        Shuffles the deck in place using the Fisher-Yates algorithm.

        Parameters
        ----------
        reset : bool
            Set to True to reset the deck and shuffle from the original 52
            cards. Otherwise, shuffle only the remaining cards in the deck.
        """
        # reset the deck to have 52 cards again, if specified
        if reset:
            self.reset()

        # grab the number of existing cards
        n = self.countCards()

        # only reshuffle if there are two or more cards in the deck
        if n > 1:
            for i in range(n-1, 0, -1):
                j = random.randint(0, i)
                if i != j:
                    self._cards[i], self._cards[j] = self._cards[j], self._cards[i]

    def dealOneCard(self):
        """
        Deals the top-most card of the deck if the deck is not empty.

        Returns
        ----------
        card.Card
            The top card in the deck.

        Raises
        ----------
        IndexError
            When the deck is empty.
        """
        if self.countCards() == 0:
            raise IndexError("Cannot deal from empty deck. Please reset or "
                "reshuffle the deck first.")
        return self._cards.pop()

    def dealNCards(self, n):
        """
        Deals the n top-most cards of the deck.

        Parameters
        ----------
        n : int
            The number of cards to deal.

        Returns
        ----------
        List[card.Card]
            The top n cards in the deck.

        Raises
        ----------
        IndexError
            When there are fewer than n cards remaining in the deck.
        """
        if self.countCards() < n:
            raise IndexError(f"Less than {n} cards are left to deal. Please "
                "reshuffle the deck first by calling shuffle().")
        return [self._cards.pop() for _ in range(n)]

    def dealRandomCard(self):
        """
        Deals a random card from the deck if the deck is not empty.

        Returns
        ----------
        card.Card
            A randomly chosen card.

        Raises
        ----------
        IndexError
            When the deck is empty.

        """
        num_cards = self.countCards()
        if num_cards == 0:
            raise IndexError("Cannot deal from empty deck. Please reshuffle "
                "the deck first by calling shuffle().")
        idx = random.randint(0, num_cards - 1)
        return self._cards.pop(idx)

    def reset(self):
        """
        Creates a fresh, sorted 52-card deck.
        """
        # note the leading single underscore _ convention to indicate that this
        # is a private variable of the class and is not to be accessed like the
        # rest of the class's API.
        self._cards = []
        for suit in Suit:
            for rank in Rank:
                card = Card(suit, rank)
                self._cards.append(card)

    def countCards(self):
        """
        Gets the current number of cards in the deck.
        
        Returns
        ----------
        int
            The number of cards in the deck.
        """
        return len(self._cards)

    def print(self):
        """
        Prints the deck of the cards to stdout.
        """
        for c in self._cards:
            print(c.name)
