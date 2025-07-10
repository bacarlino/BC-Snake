from pathlib import Path
import random

import pygame

from src.app_config import WINDOW_W, WINDOW_H
import src.ui.ui_config as ui_cfg


pygame.font.init()


def get_pixelfont(size):
    base_path = Path(__file__).parent.parent.parent
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
    for point in range((ui_cfg.WINDOW_W // cell_size)):
        border.append((point * cell_size, 0))
        border.append((point * cell_size, (ui_cfg.WINDOW_H - cell_size)))
    for point in range(ui_cfg.WINDOW_H // cell_size):
        border.append((0, point * cell_size))
        border.append((ui_cfg.WINDOW_W - cell_size, point * cell_size))
    return border


def draw_border(window, border, cell_size):
    for coordinate in border:
        pygame.draw.rect(
            window, ui_cfg.BLUE, ((coordinate), (cell_size - 4, cell_size - 4)), border_radius=ui_cfg.BORDER_RADIUS
        )


class TitleBanner:
    def __init__(self):
        self.surf = get_pixelfont(400).render("SNAKE", True, ui_cfg.PINK)
        self.rect = self.surf.get_rect()

    def draw(self, window):
        window.blit(self.surf, self.rect)


class NameBanner:
    def __init__(self):
        self.surf = get_pixelfont(50).render("Brandon Carlino's", False, ui_cfg.LT_BLUE)
        self.rect = self.surf.get_rect()

    def draw(self, window):
        window.blit(self.surf, self.rect)


class PressSpaceBanner:
    def __init__(self):
        self.surf = get_pixelfont(40).render("SPACE: Start", False, ui_cfg.LT_BLUE)
        self.rect = self.surf.get_rect()

    def draw(self, window):
        window.blit(self.surf, self.rect)


class PressSpaceEscBanner:
    def __init__(self):
        self.surf = get_pixelfont(40).render("SPACE: Confirm" + " " * 15 + "ESC: Back", False, ui_cfg.LT_BLUE)
        self.rect = self.surf.get_rect()

    def draw(self, window):
        window.blit(self.surf, self.rect)


class MatchOverBanner:
    def __init__(self):
        self.surf = get_pixelfont(100).render("MATCH OVER", True, ui_cfg.AQUA)
        self.rect = self.surf.get_rect()

    def draw(self, window):

        window.blit(self.surf, self.rect)


class GameOverBanner:
    def __init__(self):
        self.surf = get_pixelfont(100).render("GAME OVER", True, ui_cfg.AQUA)
        self.rect = self.surf.get_rect()

    def draw(self, window):
        window.blit(self.surf, self.rect)


class PausedBanner:
    def __init__(self):
        self.surf = get_pixelfont(100).render("PAUSED", True, ui_cfg.AQUA)
        self.rect = self.surf.get_rect()

    def draw(self, window):
        window.blit(self.surf, self.rect)


class WordBanner:
    def __init__(self, text="WordBanner", antialias=False, color=None, size=50):
        self.surf = get_pixelfont(size).render(text, antialias, color)
        self.rect = self.surf.get_rect()
    
    def draw(self, window):
        window.blit(self.surf, self.rect)

    def move_to(self, kw_pos):
        self.rect = self.rect.move_to(**kw_pos)


def create_score_banner(score):
    score_banner = f"{score}"
    surf = get_pixelfont(48).render(score_banner, True, ui_cfg.AQUA)
    rect = surf.get_rect(center=(ui_cfg.CENTER[0], WINDOW_H * .15))
    return surf, rect


def create_2player_score_banner(p1_score, p2_score):
    score_banner = f"PURPLE: {p2_score}                                        PINK: {p1_score}"
    surf = get_pixelfont(48).render(score_banner, True, ui_cfg.AQUA)
    rect = surf.get_rect(WINDOW_W * .15, center=ui_cfg.CENTER[0])
    return surf, rect