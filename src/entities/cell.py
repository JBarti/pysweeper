from enum import Enum
from typing import Optional


class CELL_TYPES(Enum):
    MINE=0
    EMPTY=1


class InvalidCellType(Exception):
    """Raised when invalid cell type is passed"""
    pass


class Cell:
    """Class that describes the state of each cell"""
    def __init__(self, type: CELL_TYPES, is_hidden: bool=False, adjacent_bombs: Optional[int]=None): 
        if type not in CELL_TYPES.__members__.values():
            raise InvalidCellType()
        self.type = type
        self.is_hidden = is_hidden
        self.adjacent_bombs=adjacent_bombs
