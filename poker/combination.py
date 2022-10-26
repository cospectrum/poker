from enum import Enum, auto


class Combination(Enum):
    highcard = auto()
    pair = auto()  # Two cards with the same value
    two_pairs = auto()
    three_of_kind = auto()  # Three cards with the same value
    straight = auto()  # Sequence of 5 cards in increasing value
    flush = auto()  # 5 cards of the same suit
    full_house = auto()  # three_of_kind and pair
    four_of_kind = auto()  # 4 cards of the same value
    straight_flush = auto()  # straight and flush
