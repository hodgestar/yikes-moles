""" The complete state for one game.
"""


class GameState(object):
    def __init__(self, holes=6):
        self._holes = [None] * holes

    def holes(self):
        return range(0, len(self._holes))

    def mole_at(self, i):
        return self._holes[i] is not None

    def add_mole(self, i):
        self._holes[i] = True

    def remove_mole(self, i):
        self._holes[i] = None
