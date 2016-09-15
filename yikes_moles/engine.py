""" Engine for managing scenes, events and display rendering.
"""

import pygame.display
import pygame.event
import pygame.time

import pygame.locals as pgl

from .constants import FPS
from .events import QuitEvent, SceneChangeEvent
from .wamp import WampMoles


class Engine(object):
    def __init__(self, screen, gamestate):
        self._screen = screen
        self._gamestate = gamestate
        self._scene = None

    def set_scene(self, scene):
        if self._scene is not None:
            self._scene.exit(self._gamestate)
        self._scene = scene
        if scene is not None:
            self._scene.enter(self._gamestate)

    def run(self):
        wamp = WampMoles()
        wamp.start()

        clock = pygame.time.Clock()

        while True:
            events = pygame.event.get()
            for ev in events:
                if QuitEvent.matches(ev) or ev.type == pgl.QUIT:
                    self.set_scene(None)
                    break
                elif SceneChangeEvent.matches(ev):
                    self.set_scene(ev.scene)
                else:
                    self._scene.event(ev, self._gamestate)
            if self._scene is None:
                break

            # Advance time on the world
            # Time is assumed to flow perfectly, so no dt parameter for now
            self._scene.tick(self._gamestate)
            self._scene.render(self._screen, self._gamestate)

            pygame.display.flip()
            clock.tick(FPS)

        wamp.join()
