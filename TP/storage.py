import json
from crew import build_fleet

def save_fleet(fleet, filename):
    data = fleet.to_dict()
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=2, ensure_ascii=False)
        
def load_fleet(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            data = json.load(file)
            fleet = build_fleet(data)
    except FileNotFoundError:
        raise ValueError(f"Aucune sauvegarde \"{path}\"")
    except json.JSONDecodeError:
        raise ValueError(f"la sauvergarde \"{path}\" est corrompue")
    except KeyError:
        raise ValueError(f"la sauvergarde \"{path}\" est incomplète")
    except TypeError:
        raise ValueError(f"la sauvergarde \"{path}\" est corrompue")
    return fleet
        