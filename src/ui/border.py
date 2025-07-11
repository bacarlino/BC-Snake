import pygame

from src.ui import ui_config


class Border:

    def __init__(self, dimensions: tuple, cell_size: int, color=(255, 255, 255)) -> None:
        self.coord_list = []
        self.dimensions = dimensions
        self.cell_size = cell_size
        self.color = color
        self.create_border()
    
    def create_border(self) -> None:
        self.append_top_bottom_border()
        self.append_left_right_border()

    def append_top_bottom_border(self) -> None:
        for point in range(self.dimensions[0] // self.cell_size):
            self.coord_list.append((point * self.cell_size, 0))
            self.coord_list.append((point * self.cell_size, (self.dimensions[1]- self.cell_size)))
    
    def append_left_right_border(self) -> None:
        for point in range(self.dimensions[1] // self.cell_size):
            self.coord_list.append((0, point * self.cell_size))
            self.coord_list.append((self.dimensions[0]- self.cell_size, point * self.cell_size))

    def draw(self, window: pygame.Surface) -> None:
        for coord in self.coord_list:
            pygame.draw.rect(
                window, self.color, ((coord), (self.cell_size - 4, self.cell_size - 4)), border_radius=ui_config.BORDER_RADIUS
            )
    