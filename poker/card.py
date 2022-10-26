from enum import Enum
from dataclasses import dataclass


class Suit(Enum):
    diamonds = '♦'
    clubs = '♣'
    hearts = '♥'
    spades = '♠'


class CardValue(Enum):
    Two = 2
    Three = 3
    Four = 4
    Five = 5
    Six = 6
    Seven = 7
    Eight = 8
    Nine = 9
    Ten = 10
    Jack = 11
    Queen = 12
    King = 13
    A = 14


@dataclass
class Card:
    suit: Suit
    value: CardValue
