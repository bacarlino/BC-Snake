from pathlib import Path

import pygame


pygame.mixer.init()

sounds_path = Path(__file__).parent.parent / "assets" / "sounds"

eat_fruit_path = sounds_path / "slime_000.ogg"
collision_path = sounds_path / "explosionCrunch_001.ogg"


EAT_FRUIT_SFX = pygame.mixer.Sound(eat_fruit_path)
COLLISION_SFX = pygame.mixer.Sound(collision_path)
