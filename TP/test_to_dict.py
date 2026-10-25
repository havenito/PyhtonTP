from crew import build_fleet
from fleet_data import FLEET_DATA

fleet = build_fleet(FLEET_DATA)
fleet.spaceships[0].crew[0].act()         # Hugo Crast pilote le vaisseau.
data = fleet.to_dict()
print(data["spaceships"][0]["crew"][0])
# {'type': 'operator', 'first_name': 'Hugo', 'last_name': 'Crast', 'gender': 'M',
#  'age': 37, 'role': 'pilote', 'experience': 1}
again = build_fleet(data)
print(again.to_dict() == data)             # True