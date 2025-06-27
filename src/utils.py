from random import randint

def get_rand_coord(
        window_w: int | tuple, 
        window_h: int=None,
        cell_size: int=1
):
    
    if isinstance(window_w, tuple):
        cell_size = window_h
        window_w, window_h = window_w
    return (
        randint(0, window_w // cell_size - 1) * cell_size,
        randint(0, window_h // cell_size - 1) * cell_size
    )


def align_center_to_grid(dimensions, cell_size):
    horizontal = ((dimensions[0] // cell_size) // 2) * cell_size
    vertical = ((dimensions[1] // cell_size) // 2) * cell_size

    return (horizontal, vertical)