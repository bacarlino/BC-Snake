from pathlib import Path
import random

import pygame

import src.config as cfg


pygame.init()

def get_pixelfont(size):
    base_path = Path(__file__).parent.parent
    font_path = base_path / "assets" / "fonts" / "Pixeltype.ttf"

    return pygame.font.Font(str(font_path), size)


def rand_rgb():
    return (
        random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
    )

menu_font = get_pixelfont(40)
menu_font.align = pygame.FONT_CENTER
MENU_FONT = menu_font

highlight_font = get_pixelfont(50)
highlight_font.align = pygame.FONT_CENTER
HIGHTLIGHT_FONT = highlight_font


sub_font = get_pixelfont(30)
sub_font.align = pygame.FONT_CENTER
SUB_FONT = sub_font


def create_border(cell_size):
    border = []
    for point in range((cfg.WINDOW_W // cell_size)):
        border.append((point * cell_size, 0))
        border.append((point * cell_size, (cfg.WINDOW_H - cell_size)))
    for point in range(cfg.WINDOW_H // cell_size):
        border.append((0, point * cell_size))
        border.append((cfg.WINDOW_W - cell_size, point * cell_size))
    return border


def draw_border(window, border, cell_size):
    for coordinate in border:
        pygame.draw.rect(
            window, cfg.BLUE, ((coordinate), (cell_size - 4, cell_size - 4)), border_radius=cfg.BORDER_RADIUS
        )

    
def create_title():
    surf = get_pixelfont(400).render("SNAKE", True, cfg.PINK)
    rect = surf.get_rect(center = (cfg.WINDOW_W / 2, cfg.WINDOW_H * 0.4))
    return surf, rect
    

def create_ping_pang():
    surf = get_pixelfont(50).render("Brandon Carlino's", True, cfg.LT_BLUE)
    rect = surf.get_rect(midbottom=(cfg.WINDOW_W / 2, cfg.WINDOW_H * 0.15))
    return surf, rect


def create_press_space():     
    surf = get_pixelfont(50).render("Press SPACE to start", True, cfg.LT_BLUE)
    rect = surf.get_rect(midtop=(cfg.WINDOW_W / 2, cfg.WINDOW_H * 0.85))
    return surf, rect


def create_press_space_enter():
    surf = get_pixelfont(50).render(
        "Press ENTER to select / SPACE to start", True, cfg.LT_BLUE
    )
    rect = surf.get_rect(midbottom=(cfg.WINDOW_W / 2, cfg.WINDOW_H - 64))
    return surf, rect


def create_game_over():     
    surf = get_pixelfont(100).render("GAME OVER", True, cfg.AQUA)
    rect = surf.get_rect(midtop=(cfg.WINDOW_W / 2, cfg.WINDOW_H / 2))
    return surf, rect


def create_match_over():     
    surf = get_pixelfont(100).render("MATCH OVER", True, cfg.AQUA)
    rect = surf.get_rect(midtop=(cfg.WINDOW_W / 2, cfg.WINDOW_H / 2))
    return surf, rect


def create_score_banner(score):
    score_banner = f"{score}"
    surf = get_pixelfont(48).render(score_banner, True, cfg.AQUA)
    rect = surf.get_rect(center=(cfg.CENTER[0], cfg.WINDOW_H * .15))
    return surf, rect


def create_2player_score_banner(p1_score, p2_score):
    score_banner = f"PURPLE: {p2_score}                                        PINK: {p1_score}"
    surf = get_pixelfont(48).render(score_banner, True, cfg.AQUA)
    rect = surf.get_rect(center=(cfg.CENTER[0], cfg.WINDOW_W * .15))
    return surf, rect


TITLE_SURF, TITLE_RECT = create_title()
PING_PANG_SURF, PING_PANG_RECT = create_ping_pang()
PRESS_SPACE_SURF, PRESS_SPACE_RECT = create_press_space()
GAME_OVER_SURF, GAME_OVER_RECT = create_game_over()
MATCH_OVER_SURF, MATCH_OVER_RECT = create_match_over()