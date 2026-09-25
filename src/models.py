from enum import Enum

class CellType(Enum):
    WALL = "wall"
    PACGUM = "pacgum"
    SUPER_PACGUM = "super_pacgum"
    EMPTY = "empty"

class Direction(Enum):
    UP = "up"
    DOWN = "down"
    RIGHT = "right"
    LEFT = "left"