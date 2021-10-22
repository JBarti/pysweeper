from random import choices
from .cell import (
    Cell,
    CELL_TYPES,
)
from typing import List

class Map:
    def __init__(self, cols, rows, cells=None, cell_adjacency_map=None):
        if not cells:
            cells = []
        if not cell_adjacency_map:
            cell_adjacency_map = {}

        self.cols = cols
        self.rows = rows
        self.cells = cells


def generate_random_map(rows, cols):
    cell_types_and_weights = {
        CELL_TYPES.MINE: 1,
        CELL_TYPES.EMPTY: 5,
    }

    cell_types = [
        choices(
            population=list(cell_types_and_weights.keys()), 
            weights=list(cell_types_and_weights.values()), 
            k=cols
        )
        for _ in range(rows)
    ]

    cells = [
        [
            Cell(type=cell_type)
            for cell_type in row
        ]
        for row in cell_types
    ]

    cells = _calculate_adjacent_bombs_for_cells(cells, rows, cols)

    return Map(
        rows=rows,
        cols=cols,
        cells=cells,
    )


def reveal_cell(map: Map, cell_row: int, cell_col: int):
    current_cell = map.cells[cell_row][cell_col]
    if current_cell.type == CELL_TYPES.MINE:
        current_cell.is_hidden = False

    adjacency_map = _build_adjacency_map(map.cells, map.rows, map.cols)
    stack = [] + adjacency_map[current_cell]
    while stack:
        stacked_cell = stack.pop()
        if stacked_cell.type == CELL_TYPES.MINE or stacked_cell.is_hidden == False:
            return
        stacked_cell.is_hidden = False
        if stacked_cell.adjacent_bombs == 0:
            return
        stack += adjacency_map[stacked_cell]


def _build_adjacency_map(cell_grid: List[List[Cell]], rows: int, cols: int): 
    adjacency_map = {
    }

    for row_num in range(rows):
        for col_num in range(cols):
            current_cell = cell_grid[row_num][col_num]
            adjacent_positions = _get_adjacent_positions(row_num, col_num, rows - 1, cols - 1)
            adjacent_cells = [
                cell_grid[row][col]
                for row, col in adjacent_positions
            ]

            adjacency_map[current_cell] = adjacent_cells

    return adjacency_map


def _calculate_adjacent_bombs_for_cells(cell_grid: List[List[Cell]], rows, cols):
    adjacency_map = _build_adjacency_map(cell_grid, rows, cols)
    for cell in adjacency_map.keys():
        adjacent_bomb_cells = [
            adjacent_cell
            for adjacent_cell in adjacency_map[cell]
            if adjacent_cell.type == CELL_TYPES.MINE
        ]
        cell.adjacent_bombs = len(adjacent_bomb_cells)

    return cell_grid


def _get_adjacent_positions(row_num, col_num, max_rows, max_cols):
    adjacent_positions = [
        (row_num - 1, col_num),
        (row_num + 1, col_num),
        (row_num, col_num - 1),
        (row_num, col_num + 1),
        (row_num + 1, col_num + 1),
        (row_num - 1, col_num - 1),
        (row_num - 1, col_num + 1),
        (row_num + 1, col_num - 1),
    ] 

    return [
        (row, col)
        for row, col in adjacent_positions
        if not (row < 0 or col < 0 or row > max_rows or col > max_cols)
    ]
