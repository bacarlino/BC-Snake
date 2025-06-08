import pygame


class Grid:

    def __init__(self, rows, columns, cell_size):
        self.rows = rows
        self.columns = columns
        self.cells = [[None for _ in range(self.columns)] for _ in range(self.rows)]



    def draw(self):
        for cell in self.cells:
            pygame.draw.rect()