from ephemeris_interpolator import Session


# Create a new session
session = Session()

# Add a sattelite to the session
session.add_satellite('G03')

# Add observations to the session
session.add_observation('G03', x=1, y=1, z=1, time=0)
session.add_observation('G03', x=2, y=1, z=1, time=1)
session.add_observation('G03', x=3, y=1, z=1, time=2)

# Get a satellite
my_satellite = session.get_satellite('G03')
