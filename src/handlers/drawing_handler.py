from entities.map import Map
from entities.cell import Cell, CELL_TYPES

def clear_screen():
    print("\033c")


def draw_map(map: Map):
    for row in map.cells:
        row_str = ""
        for cell in row:
            row_str += f"| {get_cell_sign(cell)} "
        print(len(row) * "+---" + "+")
        print(row_str + "|")
    print(len(map.cells[0]) * "+---" + "+")


def get_cell_sign(cell: Cell):
    if cell.is_hidden:
        return "■"
    if cell.type == CELL_TYPES.MINE:
        return "¤"
    if cell.adjacent_bombs == 0:
        return " "
    return str(cell.adjacent_bombs)
