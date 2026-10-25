from storage import save_fleet, load_fleet
from crew import build_fleet
from fleet_data import FLEET_DATA

fleet = build_fleet(FLEET_DATA)

save_fleet(fleet, "fleet.json")
print(load_fleet("fleet.json").to_dict() == fleet.to_dict())   # True
load_fleet("missing.json")
# ValueError: aucune sauvegarde « missing.json »