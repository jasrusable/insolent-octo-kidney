import random

from ephemeris_interpolator import Session


session = Session()
session.add_satellite('G03')

for i in range(86400):
    session.add_observation('G03', x=random.randint(10, 100), y=random.randint(10, 100), z=random.randint(10, 100), time=i)

my_satellite = session.get_satellite('G03')
for i in range(500):
    print(my_satellite.get_coordinate_at_time(i, polynomial_degree=10))
