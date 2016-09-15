""" Mole whacking scene. """

import pygame.draw
import pygame.locals as pgl

from ..events import QuitEvent
from .base import BaseScene


class MolesScene(BaseScene):
    def event(self, ev, gamestate):
        if ev.type == pgl.KEYDOWN:
            if ev.key in (pgl.K_q, pgl.K_ESCAPE):
                QuitEvent.post()

    def render(self, screen, gamestate):
        pygame.draw.circle(screen, (255, 0, 0), (300, 400), 40, width=4)
