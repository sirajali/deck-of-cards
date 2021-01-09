import unittest

from cards.card import Card
from cards.deck import Deck
from cards.rank import Rank
from cards.suit import Suit

class TestDeck(unittest.TestCase):
    """
    Test cases to test functionality of the cards.deck.Deck() class.
    """
    def test_deck_build(self):
        """
        Test that a deck of cards is initialized with 52 cards, in order.
        """
        deck = Deck()
        self.assertEqual(len(deck.cards), 52)
        
        ace_of_hearts = deck.cards[0]
        king_of_diamonds = deck.cards[-1]
        self.assertEqual(ace_of_hearts.rank.value, Rank.ACE.value)
        self.assertEqual(ace_of_hearts.suit.value, Suit.HEARTS.value)
        self.assertEqual(king_of_diamonds.rank.value, Rank.KING.value)
        self.assertEqual(king_of_diamonds.suit.value, Suit.DIAMONDS.value)

    def test_deal_one_card(self):
        """
        Test the dealOneCard() method returns the first card in a deck.
        """
        deck = Deck()
        dealt_card = deck.dealOneCard()
        self.assertEqual(type(dealt_card), Card)
        self.assertEqual(dealt_card.rank.value, Rank.KING.value)
        self.assertEqual(dealt_card.suit.value, Suit.DIAMONDS.value)
        self.assertEqual(len(deck.cards), 51)

    def test_deal_all_cards_one_by_one(self):
        """
        Test 52 calls to dealOneCard() return all cards in a deck.
        """
        deck = Deck()
        num_cards = 52
        for _ in range(num_cards):
            dealt_card = deck.dealOneCard()
            num_cards -= 1
            self.assertEqual(type(dealt_card), Card)
            self.assertEqual(len(deck.cards), num_cards)
        self.assertEqual(num_cards, 0)

    def test_deal_one_card_empty_deck(self):
        """
        Test that the the 53rd call to dealOneCard() will raise an error.
        """
        deck = Deck()
        for _ in range(52):
            _ = deck.dealOneCard()
        self.assertEqual(len(deck.cards), 0)
        self.assertRaises(IndexError, deck.dealOneCard)

    def test_deal_n_cards(self):
        """
        Test the dealNCards() returns the top n cards in a deck.
        """
        deck = Deck()
        num_cards = 12
        dealt_cards = deck.dealNCards(num_cards)
        self.assertEqual(type(dealt_cards), list)
        self.assertEqual(type(dealt_cards[0]), Card)
        self.assertEqual(len(dealt_cards), num_cards)
        self.assertEqual(len(deck.cards), 52 - num_cards)

    def test_deal_all_cards_at_once(self):
        """
        Test a call to dealNCards(52) will return all cards in a deck.
        """
        deck = Deck()
        num_cards = 52
        dealt_cards = deck.dealNCards(num_cards)
        self.assertEqual(type(dealt_cards), list)
        self.assertEqual(type(dealt_cards[0]), Card)
        self.assertEqual(len(dealt_cards), 52)
        self.assertEqual(len(deck.cards), 0)

    def test_deal_n_cards_too_few(self):
        """
        Test that dealing more cards than the deck has will raise an error.
        """
        deck = Deck()
        num_cards = 12
        _ = deck.dealNCards(num_cards)
        self.assertRaises(IndexError, deck.dealNCards, n=52-num_cards+1)
        self.assertRaises(IndexError, deck.dealNCards, n=9001)

    def test_deal_n_cards_empty(self):
        """
        Test that dealing cards with an empty deck will raise an error.
        """
        deck = Deck()
        num_cards = 52
        dealt_cards = deck.dealNCards(num_cards)
        self.assertEqual(len(dealt_cards), 52)
        self.assertRaises(IndexError, deck.dealNCards, n=1)

    def test_deal_random_card(self):
        """
        Test dealRandomCard() returns a random card from the deck.
        """
        deck = Deck()
        dealt_card = deck.dealRandomCard()
        self.assertEqual(type(dealt_card), Card)
        self.assertEqual(len(deck.cards), 51)

        dealt_rank = dealt_card.rank.value
        dealt_suit = dealt_card.suit.value
        for c in deck.cards:
            self.assertFalse(dealt_rank == c.rank.value and dealt_suit == c.suit.value)

    def test_deal_52_random(self):
        """
        Test 52 calls to dealRandomCard() returns all unique cards from a deck.
        """
        deck = Deck()
        dealt_cards = []
        for _ in range(52):
            dealt_cards.append(deck.dealRandomCard())
        self.assertEqual(len(dealt_cards), 52)
        self.assertEqual(len(deck.cards), 0)
        self.assertEqual(len(set(dealt_cards)), 52)

    def test_deal_random_card_empty(self):
        """
        Test that dealRandomCard() on an empty deck raises an error.
        """
        deck = Deck()
        _ = deck.dealNCards(52)
        self.assertEqual(len(deck.cards), 0)
        self.assertRaises(IndexError, deck.dealRandomCard)

    def test_shuffle_52_cards(self):
        """
        Test that shuffle() on a 52-card deck will maintain 52 Card objects.
        """
        deck = Deck()
        self.assertEqual(len(deck.cards), 52)
        deck.shuffle()
        self.assertEqual(len(deck.cards), 52)
        for c in deck.cards:
            self.assertTrue(isinstance(c, Card))

    def test_shuffle_does_not_change_cards(self):
        DEFAULT_DECK = []
        for suit in Suit:
            for rank in Rank:
                DEFAULT_DECK.append(Card(suit, rank).name)

        deck = Deck()
        deck.shuffle()
        deck_card_name_list = []
        for c in deck.cards:
            deck_card_name_list.append(c.name)
        self.assertSetEqual(set(DEFAULT_DECK), set(deck_card_name_list))
        
    def test_shuffle_some_cards(self):
        """
        Test that shuffle() will permute an existing, partially-dealt deck in
        a random order.
        """
        deck = Deck()
        num_dealt = 27
        _ = deck.dealNCards(num_dealt)
        self.assertEqual(len(deck.cards), 52 - num_dealt)
        deck.shuffle()
        self.assertEqual(len(deck.cards), 52 - num_dealt)
        for c in deck.cards:
            self.assertTrue(isinstance(c, Card))

    def test_shuffle_0_cards(self):
        """
        Test that shuffle() on an empty deck will not do anything.
        """
        deck = Deck()
        _ = deck.dealNCards(52)
        self.assertEqual(len(deck.cards), 0)
        try:
            deck.shuffle()
        except Exception:
            self.fail('test_shuffle_0_cards() raised an exception.')

    def test_deck_reset(self):
        """
        Test that reset() will return the deck to an ordered 52 cards.
        """
        deck = Deck()
        _ = deck.dealOneCard()
        deck.reset()
        self.assertEqual(len(deck.cards), 52)

    def test_shuffle_with_reset(self):
        """
        Test that shuffling a partially-dealt deck with reset=True will return
        the deck to an ordered 52 cards.
        """
        deck = Deck()
        _ = deck.dealOneCard()
        deck.shuffle(reset=True)
        self.assertEqual(len(deck.cards), 52)


if __name__ == '__main__':
    unittest.main()
