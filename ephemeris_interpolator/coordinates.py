class Coordinate(object):
    """ Represents a coordinate in 3D space.
    """
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return 'Coordinate(x={x}, y={y}, z={z})'.format(
            x=self.x,
            y=self.y,
            z=self.z,
        )
