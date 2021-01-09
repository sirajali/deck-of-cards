# Deck of Cards

Author: **Siraj Ali**

A standard deck of poker-style playing cards represented in Python.

## Problem Statement
To create a set of classes that represent a deck of poker-style playing cards (Fifty-two playing cards in four suits: hearts, spades, clubs, diamonds, with face values of Ace, 2-10, Jack, Queen, and King).

## Setup

This project was created with standard Python libraries. Python 3.7 or above is required.  

Conda 4.8.3 is used to create the environment. To create the environment using `conda`, run the following:
```bash
conda env create -f environment.yml
```
To activate the environment:
```bash
conda activate pyenv
```

## Usage
The deck of cards is comprised of four distinct classes:

### Suit
The `Suit` class, in `suit.py`, is an `Enum` class that contains an enumerated type for the four suits: Hearts, Spades, Clubs, and Diamonds.

### Rank
The `Rank` class, in `rank.py`, is an `Enum` class that contains an enumerated type for all possible card ranks (values), excluding Joker. These include the following: Ace, two, three, four, five, six, seven, eight, nine, ten, Jack, Queen, and King.

### Card
The `Card` class, in `card.py`, is an object that represents a single playing card. It has the following attributes:
* `suit`: a value of type `Suit`.
* `rank`: a value of type `Rank`.
* `name`: an easily-printable string that contains the card's rank and suit.

A card can be created as follows:
```python
from cards.card import Card
from cards.rank import Rank
from cards.suit import Suit

ace_of_hearts = Card(Suit.HEARTS, Rank.ACE)
```

To print the name of the card:
```python
print(ace_of_hearts.name)
```
The result:
```
ACE of HEARTS
```

### Deck
The `Deck` class, in `deck.py`, is an object that represents an entire 52-card deck of `Card` objects. 

The basic operations are outline below:
* `shuffle(reset)`: shuffles the deck of cards in-place using the Fisher-Yates shuffle algorithm. If the `reset` argument is set to `True`, then the deck is reset to the original 52 cards before it's shuffled (in case cards had been previously dealt). Otherwise, only the remaining cards in the deck are shuffled.
* `dealOneCard()`: returns the single, top card in the deck's list of cards. If the deck is empty, then no card is dealt and an `IndexError` exception is raised.

Additionally, I added the following extra functions:
* `dealNCards(n)`: returns a list of the top `n` cards in the deck's list of cards. If less than `n` cards remain in the deck, then no cards are dealt and an `IndexError` exception is raised.
* `dealRandomCard()`: returns a random card from the deck's list of cards. If the deck is empty, then no card is dealt and an `IndexError` exception is raised. This works just like `dealOneCard()`, but the only difference is that a random card from the deck is returned, rather than the top card.
* `reset()`: resets the deck to an unaltered, default, sorted 52-cards.
* `print()`: prints the `name` of every card in the deck's list of card to stdout.

### Example:
To create a new deck:
```python
from cards.deck import Deck

deck = Deck()
deck.print()
```
The abbreviated result:
```
ACE of HEARTS
TWO of HEARTS
.
.
.
QUEEN of DIAMONDS
KING of DIAMONDS
```

To deal one card:
```python
deck = Deck()
dealt = deck.dealOneCard()
print(f'Dealt: {dealt.name}')
print(f'Remaining cards: {deck.countCards()}')
```
The result:
```
Dealt: KING of DIAMONDS
Remaining cards: 51
```

Note that calling `dealOneCard()` 52 times will return the cards in top to bottom order of the deck. Upon a 53rd call, or if the deck is empty in general, then the following error is raised:
```
IndexError: Cannot deal from empty deck. Please reset or reshuffle the deck first.
```
Note that the above is also the case for `dealRandomCard()` if the deck is empty, or `dealNCards(n)` if there are fewer than `n` remaining cards in the deck.  

To shuffle the deck, simply call `shuffle()` on the deck:
```python
deck = Deck()
deck.print()

deck.shuffle()
deck.print()
```
The last 5 cards before shuffling:
```
NINE of DIAMONDS
TEN of DIAMONDS
JACK of DIAMONDS
QUEEN of DIAMONDS
KING of DIAMONDS
```

The last 5 cards after shuffling:
```
QUEEN of CLUBS
JACK of HEARTS
ACE of SPADES
KING of CLUBS
FOUR of DIAMONDS
```

Shuffling while resetting by calling `shuffle(reset=True)` will reset the deck to the original 52 cards before shuffling. And finally, to simply reset the deck to the original _ordered_ 52 cards, just call `reset()`.

## Testing

Python's built-in `unittest` module is used to test code functionality. To run the unit tests, execute the following:
```bash
python -m unittest discover tests -v
```
The unit tests are found in the `tests/` folder of the repository.