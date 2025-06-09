import os
from pathlib import Path
import random

import pygame

import config as cfg
from menu import Menu


pygame.init()


def get_pixelfont(size):
    this_file = Path(__file__).resolve()
    project_root = this_file.parent.parent
    font_path = project_root / "assets" / "fonts" / "Pixeltype.ttf"

    return pygame.font.Font(str(font_path), size)


def rand_rgb():
    return (
        random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
    )

def flash(colors):
    color = colors.pop(0)
    colors.append(color)
    return color

menu_font = get_pixelfont(50)
highlight_font = get_pixelfont(75)


# 1 Player / 2 Player Menu
players_menu_items = (
    "1 Player",
    "2 Player"
)

players_menu = Menu(
    players_menu_items, 0, (cfg.CENTER[0], cfg.WINDOW_H * 0.75), (1000, 150), 
    menu_font, highlight_font,
    cfg.BACKGROUND_COLOR, cfg.MAIN_COLOR, cfg.MENU_COLOR
)


# difficulty_menu_items = (
#     "Easy Street",
#     "Medium",
#     "Hard",
#     "Extreme"
# )

# difficulty_menu = Menu(
#     difficulty_menu_items, 1, (cfg.CENTER[0], cfg.WINDOW_H * 0.75), (750, 150),
#     menu_font, highlight_font,
#     cfg.BACKGROUND_COLOR, cfg.MAIN_COLOR, cfg.MENU_COLOR
# )


def create_title():
    surf = get_pixelfont(450).render("SNAKE", False, cfg.MAIN_COLOR)
    rect = surf.get_rect(center = (cfg.WINDOW_W / 2, cfg.WINDOW_H / 2))
    return surf, rect
    

def create_ping_pang():
    surf = get_pixelfont(50).render("Brandon Carlino's", False, cfg.MAIN_COLOR)
    rect = surf.get_rect(midbottom=(cfg.WINDOW_W / 2, cfg.WINDOW_H * 0.25))
    return surf, rect


def create_press_space():     
    surf = get_pixelfont(50).render("Press SPACE to begin", False, cfg.MAIN_COLOR)
    rect = surf.get_rect(midtop=(cfg.WINDOW_W / 2, cfg.WINDOW_H * 0.9))
    return surf, rect


def create_game_over():     
    surf = get_pixelfont(100).render("GAME OVER", False, cfg.DEATH_COLOR)
    rect = surf.get_rect(midtop=(cfg.WINDOW_W / 2, cfg.WINDOW_H / 2))
    return surf, rect


def create_score_banner(score):
    score_banner = f"{score}"
    surf = get_pixelfont(75).render(score_banner, False, cfg.SCORE_COLOR)
    rect = surf.get_rect(center=(cfg.CENTER[0], 75))
    return surf, rect


def create_2player_score_banner(p1_score, p2_score):
    score_banner = f"BLUE: {p2_score}                                        PINK: {p1_score}"
    surf = get_pixelfont(75).render(score_banner, False, cfg.SCORE_COLOR)
    rect = surf.get_rect(center=(cfg.CENTER[0], 75))
    return surf, rect


TITLE_SURF, TITLE_RECT = create_title()
PING_PANG_SURF, PING_PANG_RECT = create_ping_pang()
PRESS_SPACE_SURF, PRESS_SPACE_RECT = create_press_space()
GAME_OVER_SURF, GAME_OVER_RECT = create_game_over()