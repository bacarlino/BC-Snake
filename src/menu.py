import pygame

from src.input import MenuInput
from src.sounds import MENU_SCROLL, MENU_SELECT
from src.ui_elements import rand_rgb

class Menu:
    
    def __init__(
        self, 
        items=[], 
        index=0, 
        pos=(0, 0), 
        size=(0, 0),
        main_font=None, 
        highlight_font=None,
        sub_font=None,
        main_color=(255, 255, 255), 
        highlight_color=(100, 100, 255),
        background=None, 
    ):
        
        self.items = items
        self.index = index

        self.main_font = main_font
        self.highlight_font = highlight_font
        self.sub_font = sub_font

        self.background = background
        self.main_color = main_color
        self.highlight_color = highlight_color

        self.width, self.height = size

        item_width = self.width // len(self.items)
        for number, item in enumerate(self.items):
            item.initialize((item_width, self.height), (item_width * number, 0))
    
        self.surf = pygame.Surface((self.width, self.height))
        self.rect = self.surf.get_rect(midtop=pos)

        self.inputs = {
            MenuInput.SELECT: False,
            MenuInput.LEFT: False,
            MenuInput.RIGHT: False,
        }

        self.update()

    def handle_event(self, event):
        if event.key == pygame.K_SPACE:
            self.inputs[MenuInput.SELECT] = True
        if event.key == pygame.K_LEFT:
            self.inputs[MenuInput.LEFT] = True
        if event.key == pygame.K_RIGHT:
            self.inputs[MenuInput.RIGHT] = True

    def update(self):
        if self.inputs[MenuInput.SELECT] == True:
            self.select()
        if self.inputs[MenuInput.LEFT] == True:
            self.up()
        if self.inputs[MenuInput.RIGHT] == True:
            self.down()
  
        self.update_items()
        for input in self.inputs:
            self.inputs[input] = False

    def draw(self, window):
        # self.surf.fill(self.background)
        self.surf.fill("white")
        for item in self.items:
            item.draw(self.surf)
        window.blit(self.surf, self.rect)

    def up(self):
        if self.index > 0:
            MENU_SCROLL.play()
            self.index -= 1
            self.update_items()

    def down(self):
        if self.index < len(self.items) - 1:
            MENU_SCROLL.play()
            self.index += 1
            self.update_items()
    
    def select(self):
        MENU_SELECT.play()
        self.items[self.index].callback()

    def update_items(self):
        for item in self.items:
            if item == self.items[self.index]:
                item.make_main_color(self.highlight_color)
                item.set_main_font(self.highlight_font)
            else:
                item.make_main_color(self.main_color)
                item.set_main_font(self.main_font)
            item.set_sub_font(self.sub_font)
            item.make_sub_color(self.main_color)
            item.update()


class MenuItem:
        
    def __init__(self, main_text="TEXT", callback=None, sub_text="SUBTEXT"):
        self.main_text = main_text
        self.sub_text = sub_text
        self.callback = callback
        self.main_color = None
        self.sub_color = None
        self.pos = None
        self.sub_pos = None
        self.main_font = None
        self.sub_font = None

        self.main_surf = None
        self.main_rect = None

    def update(self):
        self.main_text_surf = self.main_font.render(self.main_text, True, self.main_color, bgcolor="yellow")
        self.main_text_rect = self.main_text_surf.get_rect(center=(self.main_rect.width // 2, self.main_rect.height // 2))
        
        self.sub_text_surf = self.sub_font.render(self.sub_text, True, self.sub_color, bgcolor="yellow", wraplength=self.main_rect.width)
        self.sub_text_rect = self.sub_text_surf.get_rect(center=(self.main_rect.width // 2, self.main_rect.height // 2))

    def initialize(self, size, pos):
        centerline = size[1] // 2
        self.main_surf = pygame.Surface((size[0], centerline))
        self.main_surf.fill("brown")
        self.main_rect = self.main_surf.get_rect(topleft=pos)

        self.sub_surf = pygame.Surface((size[0], centerline))
        self.sub_surf.fill("blueviolet")
        self.sub_rect = self.sub_surf.get_rect(topleft=(pos[0], centerline))

    def make_main_color(self, color):
        self.main_color = color

    def make_sub_color(self, color):
        self.sub_color = color

    def set_main_font(self, font):
        self.main_font = font

    def set_sub_font(self, sub_font):
        self.sub_font = sub_font

    def draw(self, surf):
        self.main_surf.blit(self.main_text_surf, self.main_text_rect)
        self.sub_surf.blit(self.sub_text_surf, self.sub_text_rect)

        surf.blit(self.main_surf, self.main_rect)
        surf.blit(self.sub_surf, self.sub_rect)