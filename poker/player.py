from dataclasses import dataclass

from .card import Card


Money = int


@dataclass
class Player:
    hand: tuple[Card, Card]
    money: Money
    bet: Money = 0
