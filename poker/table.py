from dataclasses import dataclass

from .player import Player
from .board import Board
from .deck import Deck


Money = int


@dataclass
class Table:
    players: list[Player]
    board: Board
    deck: Deck
    pot: Money = 0
