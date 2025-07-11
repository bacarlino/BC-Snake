from pathlib import Path
from random import randint

import pygame

from src.ui import ui_config

pygame.font.init()


def layout_title_banners(name, title, cmd_bar):
    name.rect.center = ui_config.NAME_BANNER_CENTER
    title.rect.center = ui_config.TITLE_BANNER_CENTER
    cmd_bar.rect.midbottom = ui_config.COMMAND_BAR_MIDBOTTOM


def rand_rgb():
    return (
        randint(0, 255), randint(0, 255), randint(0, 255)
    )


def get_pixelfont(size):
    base_path = Path(__file__).parent.parent.parent
    font_path = base_path / "assets" / "fonts" / "Pixeltype.ttf"

    return pygame.font.Font(str(font_path), size)
