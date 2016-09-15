""" Mole whacking scene. """

import random

import pygame.draw
import pygame.locals as pgl

from ..constants import SCREEN_SIZE
from ..events import QuitEvent
from .base import BaseScene


class Hole(object):
    def __init__(self, pos, radius):
        self.pos = pos
        self.radius = radius
        self.mole = False

    def collides(self, pos):
        dx, dy = pos[0] - self.pos[0], pos[1] - self.pos[1]
        return dx ** 2 + dy ** 2 < self.radius ** 2

    def render(self, surface):
        pygame.draw.circle(
            surface, (255, 0, 0), self.pos, self.radius, width=4)
        if self.mole:
            pygame.draw.circle(
                surface, (0, 0, 255), self.pos, self.radius - 10)


class MolesScene(BaseScene):
    def enter(self, gamestate):
        self._holes = []
        margin = 100
        holes = gamestate.holes()
        diameter = (SCREEN_SIZE[0] - 2 * margin) // len(holes)
        radius = int(diameter / 2.5)
        for i in holes:
            pos = (margin + diameter // 2 + i * diameter, 350)
            self._holes.append((i, Hole(pos, radius)))

    def event(self, ev, gamestate):
        if ev.type == pgl.KEYDOWN:
            if ev.key in (pgl.K_q, pgl.K_ESCAPE):
                QuitEvent.post()
        elif ev.type == pgl.MOUSEBUTTONDOWN:
            for i, hole in self._holes:
                if hole.collides(ev.pos):
                    gamestate.remove_mole(i)
                    break

    def tick(self, gamestate):
        for h in gamestate.holes():
            if random.random() < 0.01:
                gamestate.add_mole(h)

    def render(self, screen, gamestate):
        screen.fill((0, 0, 0))
        for i, hole in self._holes:
            hole.mole = gamestate.mole_at(i)
            hole.render(screen)
