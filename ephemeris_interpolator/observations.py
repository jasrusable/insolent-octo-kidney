from coordinates import Coordinate


class Observation(object):
    """ Represents a Coordinate at a particular time.
    """
    def __init__(self, x, y, z, time):
        self.coordinate=Coordinate(x, y, z)
        self.time = time

    def __repr__(self):
        return 'Observation(x={x}, y={y}, z={z}, time={time}'.format(
            x=self.x,
            y=self.y,
            z=self.z,
            time=self.time,
        )
