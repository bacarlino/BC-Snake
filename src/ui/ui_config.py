import pygame

from src.app_config import WINDOW_W, WINDOW_H
from src.ui.ui_helpers import get_pixelfont


CENTER = (WINDOW_W // 2, WINDOW_H // 2)
TITLE_BANNER_CENTER = (WINDOW_W // 2, WINDOW_H * 0.4)
NAME_BANNER_CENTER = (WINDOW_W // 2, WINDOW_H * 0.15)
COMMAND_BAR_MIDBOTTOM = (WINDOW_W // 2, WINDOW_H - 80)

BORDER_RADIUS = 4


# COLORS
PINK = (230,0,170)
PURPLE = (170,0,230)
BLUE = (0,21,255)
LT_BLUE = (0, 142, 255)
GREEN = (0, 255, 100)
AQUA = (0, 255, 230)

BLACK = (25, 25, 25)
WHITE = (230, 230, 230)
ORANGE = (230,95,31)
LIME = (170,230,0)
RED = (230,0,0)


# MENU STYLING
menu_font = get_pixelfont(40)
menu_font.align = pygame.FONT_CENTER
MENU_FONT = menu_font

highlight_font = get_pixelfont(50)
highlight_font.align = pygame.FONT_CENTER
HIGHTLIGHT_FONT = highlight_font

sub_font = get_pixelfont(30)
sub_font.align = pygame.FONT_CENTER
SUB_FONT = sub_font

MENU_STYLE = {            
    "main_font": MENU_FONT, 
    "highlight_font": HIGHTLIGHT_FONT,
    "sub_font": SUB_FONT,
    "main_color": PINK, 
    "highlight_color": WHITE,
    "sub_color": AQUA,
    "bg_color": BLACK, 
}
