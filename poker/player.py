from dataclasses import dataclass

from .card import Card
from .money import Money


@dataclass
class Player:
    name: str
    money: Money
    bet: Money = 0
    hand: tuple[Card, Card] | None = None
