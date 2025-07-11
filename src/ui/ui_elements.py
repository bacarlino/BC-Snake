from src.app_config import WINDOW_W, WINDOW_H
import src.ui.ui_config as ui_cfg
from src.ui.ui_helpers import get_pixelfont
    

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


class ScoreBanner:
    def __init__(self, score=0):
        self.update(score)

    def update(self, score=0):
        score_str = f"{score}"
        self.surf = get_pixelfont(48).render(score_str, True, ui_cfg.AQUA)
        self.rect = self.surf.get_rect(center=(ui_cfg.CENTER[0], WINDOW_H * .15))
        
    def draw(self, window):
        window.blit(self.surf, self.rect)


class TwoPlayerScoreBanner:
    def __init__(self, scores=(0, 0)):
        self.update(scores)

    def update(self, scores):
        self.score_str = f"PURPLE: {scores[1]}{" " * 40}PINK: {scores[0]}"
        self.surf = get_pixelfont(48).render(self.score_str, True, ui_cfg.AQUA)
        self.rect = self.surf.get_rect(center=(ui_cfg.CENTER[0], WINDOW_H * .15))

    def draw(self, window):
        window.blit(self.surf, self.rect)