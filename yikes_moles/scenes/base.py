""" Base scene class. """


class BaseScene(object):
    def enter(self, gamestate):
        """ Enter the scene. """

    def exit(self, gamestate):
        """ Leave the scene. """

    def event(self, ev, gamestate):
        """ Handle an event. """

    def render(self, screen, gamestate):
        """ Render the scene. """

    def tick(self, gamestate):
        """ Update the world based on time """
