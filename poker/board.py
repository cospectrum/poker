from .card import Card


class Board:
    cards: list[Card]

    def __init__(self, cards: list[Card] | None = None) -> None:
        self.cards = [] if cards is None else cards

    def __len__(self) -> int:
        return len(self.cards)

    def __repr__(self) -> str:
        return f'Board({self.cards})'
