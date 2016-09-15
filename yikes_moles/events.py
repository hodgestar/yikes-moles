""" Events recognized by the game engine. """

import pygame.event
import pygame.locals as pgl


class YikesMolesEvent(object):
    TYPE = "UNKNOWN"
    ATTRIBUTES = set()

    @classmethod
    def post(cls, **attributes):
        assert set(attributes.keys()) == cls.ATTRIBUTES
        ev = pygame.event.Event(
            pgl.USEREVENT, ym_type=cls.TYPE, **attributes)
        pygame.event.post(ev)

    @classmethod
    def matches(cls, ev):
        return (ev.type == pgl.USEREVENT and ev.ym_type == cls.TYPE)


class QuitEvent(YikesMolesEvent):
    TYPE = "QUIT"


class SceneChangeEvent(YikesMolesEvent):
    TYPE = "SCENE_CHANGE"
    ATTRIBUTES = {'scene'}
