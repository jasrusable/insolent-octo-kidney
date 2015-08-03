import numpy

from observations import Observation
from coordinates import Coordinate


class Satellite(object):
    """ Represents a satellite.
    """
    def __init__(self, id=None):
        self.id = id
        self.observations = []
        self.get_ordinate_polynomial_cache = None

    def __repr__(self):
        return 'Satellite(id={id})'.format(id=self.id)

    def add_observation(self, x, y, z, time):
        # Invalidate poly_func cache
        self.get_ordinate_polynomial_cache = None
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

    def get_coordinate_at_time(self, time, polynomial_degree):
        """ Returns Coordinate of a satellite at time,
        based on interpolation of observations.
        """
        if self.get_ordinate_polynomial_cache:
            if self.get_ordinate_polynomial_cache['polynomial_degree'] != polynomial_degree:
                self.get_ordinate_polynomial_cache = None

        if not self.get_ordinate_polynomial_cache:
            self.get_ordinate_polynomial_cache = {
                'x_polynomial': self.get_ordinate_polynomial('x', polynomial_degree),
                'y_polynomial': self.get_ordinate_polynomial('y', polynomial_degree),
                'z_polynomial': self.get_ordinate_polynomial('z', polynomial_degree),
                'polynomial_degree': polynomial_degree,
            }
        x = self.get_ordinate_polynomial_cache['x_polynomial'](time)
        y = self.get_ordinate_polynomial_cache['y_polynomial'](time)
        z = self.get_ordinate_polynomial_cache['z_polynomial'](time)

        return Coordinate(x=x, y=y, z=z)
