from entities.map import generate_random_map, reveal_cell
from handlers.drawing_handler import clear_screen, draw_map

new_map = generate_random_map(10, 10)
clear_screen()
draw_map(new_map)
