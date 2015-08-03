import numpy

from observations import Observation
from coordinates import Coordinate


class Satellite(object):
    """ Represents a satellite.
    """
    def __init__(self, id=None):
        self.id = id
        self.observations = []

    def __repr__(self):
        return 'Satellite(id={id})'.format(id=self.id)

    def add_observation(self, x, y, z, time):
        self.observations.append(
            Observation(x, y, z, time)
        )

    def get_ordinate_polynomial(self, ordinate, degree):
        """ Returns a numpy.poly1d function with 
        y-axis as ordinate, and x-axis as time.
        """
        x, y = [], []
        for observation in self.observations:
            x.append(observation.time)
            y.append(getattr(observation.coordinate, ordinate))
        return numpy.poly1d(numpy.polyfit(x, y, degree))

    def get_coordinate_at_time(self, time):
        """ Returns Coordinate of a satellite at time,
        based on interpolation of observations.
        """
        degree = len(self.observations) - 1
        xyz = [self.get_ordinate_polynomial(ordinate, degree)(time) for ordinate in ['x', 'y', 'z']]
        return Coordinate(x=xyz[0], y=xyz[1], z=xyz[2])
