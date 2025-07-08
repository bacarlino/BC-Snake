from pathlib import Path
import random

import pygame

import src.app_config as cfg


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


class TitleBanner:
    def __init__(self):
        self.surf = get_pixelfont(400).render("SNAKE", True, cfg.PINK)
        self.rect = self.surf.get_rect(center = (cfg.WINDOW_W // 2, cfg.WINDOW_H * 0.4))

    def draw(self, window):
        window.blit(self.surf, self.rect)


class NameBanner:
    def __init__(self):
        self.surf = get_pixelfont(50).render("Brandon Carlino's", False, cfg.LT_BLUE)
        self.rect = self.surf.get_rect(midbottom=(cfg.WINDOW_W // 2, cfg.WINDOW_H * 0.15))

    def draw(self, window):
        window.blit(self.surf, self.rect)


class PressSpaceBanner:
    def __init__(self):
        self.surf = get_pixelfont(40).render("SPACE: Start", False, cfg.LT_BLUE)
        self.rect = self.surf.get_rect(midbottom=(cfg.WINDOW_W // 2, cfg.WINDOW_H - 80))

    def draw(self, window):
        window.blit(self.surf, self.rect)


class PressSpaceEscBanner:
    def __init__(self):
        self.surf = get_pixelfont(40).render("SPACE: Confirm" + " " * 15 + "ESC: Back", False, cfg.LT_BLUE)
        self.rect = self.surf.get_rect(midbottom=(cfg.WINDOW_W // 2, cfg.WINDOW_H - 80))

    def draw(self, window):
        window.blit(self.surf, self.rect)


class MatchOverBanner:
    def __init__(self):
        self.surf = get_pixelfont(100).render("MATCH OVER", True, cfg.AQUA)
        self.rect = self.surf.get_rect(midtop=(cfg.WINDOW_W / 2, cfg.WINDOW_H / 2))

    def draw(self, window):

        window.blit(self.surf, self.rect)


class GameOverBanner:
    def __init__(self):
        self.surf = get_pixelfont(100).render("GAME OVER", True, cfg.AQUA)
        self.rect = self.surf.get_rect(midtop=(cfg.WINDOW_W / 2, cfg.WINDOW_H / 2))

    def draw(self, window):
        window.blit(self.surf, self.rect)


class PausedBanner:
    def __init__(self):
        self.surf = get_pixelfont(100).render("PAUSED", True, cfg.AQUA)
        self.rect = self.surf.get_rect(midtop=(cfg.WINDOW_W / 2, cfg.WINDOW_H / 2))

    def draw(self, window):
        window.blit(self.surf, self.rect)


class WordBanner:
    def __init__(self, text="WordBanner", antialias=False, color=None, size=50, kw_pos={"topleft": (0, 0)}):
        self.surf = get_pixelfont(size).render(text, antialias, color)
        self.rect = self.surf.get_rect(**kw_pos)
    
    def draw(self, window):
        window.blit(self.surf, self.rect)

    def move_to(self, kw_pos):
        self.rect = self.rect.move_to(**kw_pos)


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