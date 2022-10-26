from dataclasses import dataclass

from .player import Player
from .board import Board
from .deck import Deck
from .money import Money


@dataclass
class Table:
    players: list[Player]
    board: Board
    deck: Deck
    pot: Money = 0
