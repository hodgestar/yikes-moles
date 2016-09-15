""" Run Yikes! Moles!
"""

import pygame
import pygame.locals as pgl

from .constants import SCREEN_SIZE, TITLE
from .engine import Engine
from .gamestate import GameState
from .scenes.moles import MolesScene


def main():
    pygame.display.init()
    pygame.font.init()

    pygame.display.set_mode(SCREEN_SIZE, pgl.SWSURFACE)
    pygame.display.set_caption(TITLE)

    screen = pygame.display.get_surface()
    gamestate = GameState()
    engine = Engine(screen, gamestate)
    engine.set_scene(MolesScene())

    engine.run()
