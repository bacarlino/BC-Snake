import pygame

from src.input import MenuInput
from src.sounds import MENU_SCROLL, MENU_SELECT


class MenuGrid:

    def __init__(self, item_grid, pos, size, colors):
        self.pos = pos
        self.size = size
        self.colors = colors
        self.item_grid = self.check_list_format(item_grid)
        self.menu_list = []
        self.row_size = (size[0], size[1] // len(item_grid))
        self.create_menu_list()
        self.focus_index = 0
        self.focused_menu = self.menu_list[self.focus_index]
        self.set_focus(self.focused_menu)
    

        self.inputs = {
            MenuInput.UP: False,
            MenuInput.DOWN: False
        }

    def displays_title(self):
        return False

    def check_list_format(self, item_grid):
        return [item_grid] if not isinstance(item_grid[0], list) else item_grid
        
    def create_menu_list(self):
        track_pos = self.pos
        for item_list in self.item_grid:
            self.menu_list.append(
                Menu(item_list, track_pos, self.row_size, **self.colors)
            )
            track_pos = (self.pos[0], self.pos[1] + self.row_size[1])

    def handle_event(self, event):
        if event.key == pygame.K_DOWN or event.key == pygame.K_s:
            self.inputs[MenuInput.DOWN] = True
        if event.key == pygame.K_UP or event.key == pygame.K_w:
            self.inputs[MenuInput.UP] = True

        self.focused_menu.handle_event(event)

    def update(self):
        if self.inputs[MenuInput.UP]:
            self.up()
        if self.inputs[MenuInput.DOWN]:
            self.down()
        self.focused_menu.update()
        
        for input in self.inputs:
            self.inputs[input] = False

    def draw(self, window):
        for menu in self.menu_list:
            menu.draw(window)

    def up(self):
        print("up() called")
        if self.focus_index > 0:
            MENU_SCROLL.play()
            old_menu = self.focused_menu
            self.focus_index -= 1
            # self.focused_menu = self.menu_list[self.focus_index]
            self.set_focus(old_menu)

    def down(self):
        print("down() called")
        if self.focus_index < len(self.menu_list) - 1:
            MENU_SCROLL.play()
            old_menu = self.focused_menu
            self.focus_index += 1
            self.set_focus(old_menu)
            # self.focused_menu = self.menu_list[self.focus_index]
    
    def set_focus(self, old_menu):
        self.clear_is_focused()
        self.focused_menu = self.menu_list[self.focus_index]
        self.focused_menu.is_focused = True
        self.focused_menu.index = self.change_focus_index(old_menu, self.focused_menu)
        self.update_items()

    def change_focus_index(self, old_menu, new_menu):
        old_index = old_menu.index
        if old_index <= len(new_menu.items) - 1:
            return old_index
        else:
            return len(new_menu.items) - 1
    
    def clear_is_focused(self):
        for menu in self.menu_list:
            menu.is_focused = False
    
    def update_items(self):
        for menu in self.menu_list:
            menu.update_items()

    def update_sub_text(self, text):
        self.focused_menu.update_sub_text(text)
        self.update_items()



class Menu:
    
    def __init__(
        self, 
        items=[], 
        pos=(0, 0), 
        size=(0, 0),
        index=0, 
        main_font=None, 
        highlight_font=None,
        sub_font=None,

        main_color=(255, 255, 255), 
        highlight_color=(100, 100, 255),
        sub_color = None,
        bg_color=None, 
    ):
        
        self.items = items
        self.index = index
        
        self.is_focused = True

        self.main_font = main_font
        self.highlight_font = highlight_font
        self.sub_font = sub_font

        self.main_color = main_color
        self.highlight_color = highlight_color
        self.sub_color = sub_color
        self.bg_color = bg_color

        self.width, self.height = size
        self.width = self.width * (0.3 + (0.12 * len(self.items)))
        item_width = (self.width // len(self.items))
        
        for number, item in enumerate(self.items):
            item.initialize((item_width, self.height), (item_width * number, 0), self.bg_color)
    
        self.surf = pygame.Surface((self.width, self.height))
        self.rect = self.surf.get_rect(midtop=pos)

        self.inputs = {
            MenuInput.SELECT: False,
            MenuInput.LEFT: False,
            MenuInput.RIGHT: False,
        }

        self.update()
        self.update_items()

    def handle_event(self, event):
        if event.key == pygame.K_SPACE:
            self.inputs[MenuInput.SELECT] = True
        if event.key == pygame.K_LEFT:
            self.inputs[MenuInput.LEFT] = True
        if event.key == pygame.K_RIGHT:
            self.inputs[MenuInput.RIGHT] = True

    def update(self):
        if not self.is_focused:
            return
        if self.inputs[MenuInput.SELECT] == True:
            self.select()
        if self.inputs[MenuInput.LEFT] == True:
            self.up()
        if self.inputs[MenuInput.RIGHT] == True:
            self.down()
  
        # update items here and in up() down()? doesn't seem necessary
        # self.update_items()
        
        for input in self.inputs:
            self.inputs[input] = False

    def draw(self, window):
        self.surf.fill(self.bg_color)
        for item in self.items:
            item.draw(self.surf)
        window.blit(self.surf, self.rect)

    def up(self):
        if self.index > 0:
            MENU_SCROLL.play()
            self.index -= 1
            
            self.update_items() # here and update? update seems wrong

    def down(self):
        if self.index < len(self.items) - 1:
            MENU_SCROLL.play()
            self.index += 1
            self.update_items() # here and update? update seems wrong
    
    def select(self):
        MENU_SELECT.play()
        self.items[self.index].callback()

    def update_items(self):
        for item in self.items:
            if self.is_focused and item == self.items[self.index]:
                item.make_main_color(self.highlight_color)
                item.set_main_font(self.highlight_font)
            else:
                item.make_main_color(self.main_color)
                item.set_main_font(self.main_font)
            item.set_sub_font(self.sub_font)
            item.make_sub_color(self.sub_color)
            item.update()

    def displays_title(self):
        return True
        
    def update_sub_text(self, text):
        self.items[self.index].sub_text = text


class MenuItem:
        
    def __init__(self, main_text="MAIN TEXT", callback=None, sub_text="SUB TEXT"):
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
        self.main_surf.fill((self.bg_color))
        self.sub_surf.fill((self.bg_color))
    
        self.main_text_surf = self.main_font.render(self.main_text, True, self.main_color)
        self.main_text_rect = self.main_text_surf.get_rect(center=(self.main_rect.width // 2, self.main_rect.height * 0.4))
        
        self.sub_text_surf = self.sub_font.render(self.sub_text, True, self.sub_color, wraplength=int(self.sub_rect.width * .8))
        self.sub_text_rect = self.sub_text_surf.get_rect(midtop=(self.sub_rect.width // 2, 0))

    def initialize(self, size, pos, bg_color):
        self.bg_color = bg_color
        centerline = size[1] * 0.4
        self.main_surf = pygame.Surface((size[0], centerline))
        self.main_rect = self.main_surf.get_rect(topleft=pos)

        self.sub_surf = pygame.Surface((size[0], size[1]-centerline))
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

    def get_sub_text(self):
        if callable(self.sub_text):
            return self.sub_text_update_func()
        else:
            return self.sub_text