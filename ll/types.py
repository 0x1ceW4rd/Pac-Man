from dataclasses import dataclass
from enum import Enum


class Direction(Enum):
    """Represent the four possible movement directions."""

    UP = "up"
    DOWN = "down"
    LEFT = "left"
    RIGHT = "right"
    NONE = "none"


class GameState(Enum):
    """Represent the global state of the game."""

    MENU = "menu"
    PLAYING = "playing"
    PAUSED = "paused"
    GAME_OVER = "game_over"
    VICTORY = "victory"


@dataclass(frozen=True)
class Position:
    """Represent a position inside the maze."""

    x: int
    y: int