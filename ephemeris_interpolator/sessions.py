from satellites import Satellite


class Session(object):
    def __init__(self):
        self.satellites = []

    def add_satellite(self, id):
        if self.get_satellite(id):
            raise Exception("Failed to add satellite. Satellite with id: {id} already exists."
                .format(id=id))
        self.satellites.append(
            Satellite(id)
        )

    def remove_satellite(self, id):
        if not self.get_satellite(id):
            raise Exception("Failed to remove satellite. Satellite with id: {id} does not exist."
                .format(id=id))
        for satellite in self.satellites:
            if satellite.id == id:
                self.satellites.remove(satellite)

    def get_satellite(self, id):
        for satellite in self.satellites:
            if satellite.id == id:
                return satellite
        return None

    def add_observation(self, satellite_id, x, y, z, time):
        satellite = self.get_satellite(satellite_id)
        if not satellite:
            raise Exception("Failed to add observation. Satellite with id: {id} does not exist."
                .format(id=satellite_id))
        satellite.add_observation(x, y, z, time)
