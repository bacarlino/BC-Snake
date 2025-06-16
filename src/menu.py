import pygame


class Menu:
    
    def __init__(
        self, 
        items=[], 
        index=0, 
        pos=(0, 0), 
        size=(0, 0),
        main_font=None, 
        highlight_font=None,
        background=None, 
        main_color=(255, 255, 255), 
        highlight_color=(100, 100, 255)
    ):
        
        self.menu_items = items
        self.index = index

        self.main_font = main_font
        self.highlight_font = highlight_font

        self.background = background
        self.main_color = main_color
        self.highlight_color = highlight_color

        self.width, self.height = size

        self.surf = pygame.Surface((self.width, self.height))
        self.rect = self.surf.get_rect(center=pos)

        self.update()
        self.align_items()

    def update(self):
        for item in self.menu_items:
            if item == self.menu_items[self.index]:
                item.make_color(self.highlight_color)
                item.set_font(self.highlight_font)
            else:
                item.make_color(self.main_color)
                item.set_font(self.main_font)
            item.update()

    def draw(self, surf):
        self.surf.fill(self.background)
        for item in self.menu_items:
            item.draw(self.surf)
        surf.blit(self.surf, self.rect)

    def up(self):
        if self.index < len(self.menu_items) - 1:
            self.index += 1
            self.update()
    
    def down(self):
        if self.index > 0:
            self.index -= 1
            self.update()

    def select(self):
        self.menu_items[self.index].callback()

    def align_items(self):
        
        segments = len(self.menu_items) + 1
        multiplier = (self.width / segments) / self.width

        for i, item in enumerate(self.menu_items, start=1):

            x = self.width * (multiplier * i)
            item.set_pos((x, self.height / 2))
        

class MenuItem:
        
    def __init__(self, text="TEXT", callback=None, font=None, color=(255, 255, 255), size=12, pos=(0, 0)):    
        self.text = text
        self.callback = callback
        self.color = color
        self.pos = pos
        self.font = font

    def update(self):
        self.surf = self.font.render(self.text, True, self.color)
        self.rect = self.surf.get_rect(center=self.pos)

    def make_color(self, color):
        self.color = color

    def set_font(self, font):
        self.font = font

    def draw(self, surf):
        surf.blit(self.surf, self.rect)

    def set_pos(self, pos):
        self.pos = pos
        self.rect.center = pos