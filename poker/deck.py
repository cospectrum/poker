import random

from .card import Card, Suit, CardValue


class Deck:
    cards: list[Card]

    def __init__(self, cards: list[Card] | None = None) -> None:
        if cards is None:
            cards = [
                Card(suit=suit, value=value)
                for suit in Suit
                for value in CardValue
            ]
        self.cards = cards

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def take_card(self) -> Card:
        return self.cards.pop()

    def __len__(self) -> int:
        return len(self.cards)

    def __repr__(self) -> str:
        return f'Deck({self.cards})'
