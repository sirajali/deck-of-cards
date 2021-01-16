import unittest

from cards.card import Card
from cards.rank import Rank
from cards.suit import Suit

class TestCard(unittest.TestCase):
    """
    Test cases to test functionality of the cards.card.Card() class.
    """
    def test_correct_initialization(self):
        """
        Assert that the suit and rank of a newly instantiated Card is correct.
        """
        king_of_diamonds = Card(Suit.DIAMONDS, Rank.KING)
        self.assertEqual(king_of_diamonds.rank.value, Rank.KING.value)
        self.assertEqual(king_of_diamonds.suit.value, Suit.DIAMONDS.value)

    def test_suit_equality(self):
        """
        Assert that the suit values of two different cards belonging to the
        same suit are equal.
        """
        ace_of_hearts = Card(Suit.HEARTS, Rank.ACE)
        two_of_hearts = Card(Suit.HEARTS, Rank.TWO)
        self.assertEqual(ace_of_hearts.suit.value, two_of_hearts.suit.value)

    def test_rank_equality(self):
        """
        Assert that the rank values of two different cards belonging to the
        different suit, but with the same ranks, are equal.
        """
        jack_of_clubs = Card(Suit.CLUBS, Rank.JACK)
        jack_of_spades = Card(Suit.SPADES, Rank.JACK)
        self.assertEqual(jack_of_clubs.rank.value, jack_of_spades.rank.value)

    def test_rank_value(self):
        """
        Assert that the values of differently-ranked cards compare correctly.
        """
        ace_of_hearts = Card(Suit.HEARTS, Rank.ACE)
        two_of_hearts = Card(Suit.HEARTS, Rank.TWO)
        king_of_clubs = Card(Suit.CLUBS, Rank.KING)

        # Two minus Ace = 2 - 1 = 1
        self.assertEqual(two_of_hearts.rank.value - ace_of_hearts.rank.value, 1)

        # King minus Ace = 13 - 1 = 12
        self.assertEqual(king_of_clubs.rank.value - ace_of_hearts.rank.value, 12)

if __name__ == '__main__':
    unittest.main()