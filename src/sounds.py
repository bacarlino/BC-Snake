from pathlib import Path

import pygame


pygame.mixer.init()

sounds_path = Path(__file__).parent.parent / "assets" / "sounds"

menu_scroll_path = sounds_path / "click4.ogg"
menu_select_path = sounds_path / "switch1.ogg"
eat_fruit_path = sounds_path / "slime_000.ogg"
collision_path = sounds_path / "explosionCrunch_001.ogg"


MENU_SCROLL = pygame.mixer.Sound(menu_scroll_path)
MENU_SELECT = pygame.mixer.Sound(menu_select_path)
EAT_FRUIT_SFX = pygame.mixer.Sound(eat_fruit_path)
COLLISION_SFX = pygame.mixer.Sound(collision_path)
