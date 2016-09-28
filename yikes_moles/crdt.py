""" A CvRDT for maintain information about living and dead moles. """

from hyperloglog import HyperLogLog


class MolesState(object):
    """ State of the mole nation. """

    DEAD_MOLE_ACCURACY = 0.01

    def __init__(self):
        self._dead_moles = set()
        self._live_moles = {}
        self._dead_mole_count = HyperLogLog(self.DEAD_MOLE_ACCURACY)

    def to_dict(self):
        """ Serialize to a dictionary. """
        return {
            "live_moles": self._live_moles,
            "dead_moles": list(self._dead_moles),
            "dead_mole_count": self._dead_mole_count.__getstate__(),
        }

    @classmethod
    def from_dict(cls, d):
        """ Parse from a dictionary. """
        moles = cls()
        moles._dead_moles.updated(d["dead_moles"])
        moles._live_moles.update(d["live_moles"])
        moles._dead_mole_count.__setstate__(d["dead_mole_count"])
        return moles

    def merge(self, other):
        """ Merge another state into this one. """
        self._dead_moles.update(other._dead_moles)
        for k, v in other._live_moles.items():
            self._like_moles.setdefault(k, set())
            self._like_moles[k].update(v)
        self._dead_mole_count.update(other._dead_mole_count)
