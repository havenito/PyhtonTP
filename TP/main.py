from crew import *
from fleet_data import FLEET_DATA
from storage import save_fleet, load_fleet

crew = [
{"first_name": "Bel", "last_name": "Riose", "gender": "M", "age": 48, "role": "commandant"},
{"first_name": "Gaal", "last_name": "Dornick", "gender": "F", "age": 34, "role": "technicien"},
{"first_name": "Hugo", "last_name": "Crast", "gender": "M", "age": 37, "role": "pilote"},
{"first_name": "Salvor", "last_name": "Hardin", "gender": "F", "age": 28, "role": "armurier"},
{"first_name": "Novi", "last_name": "Sura", "gender": "F", "age": 25, "role": "entretien"},
]

fleet = build_fleet(FLEET_DATA)

def save_menu(fleet):
    path = input("Fichier de sauvegarde [fleet.json] : ")
    if path == "":
        path = "fleet.json"
    save_fleet(fleet, path)
    print(f"Flotte sauvegardée dans {path}")

def load_menu(fleet):
    path = input("Fichier de chargement [fleet.json] : ")
    if path == "":
        path = "fleet.json"
    try:
        new_fleet = load_fleet(path)
    except ValueError as erreur: 
        print(f"Chargement impossible : {erreur}")
        return fleet
    print(f"Flotte {new_fleet.name} chargée depuis {path}")
    return new_fleet

def menu():
    global fleet
    while True:
        print("===== Flotte marchande - Gestion de l'équipage =====")
        print("[1] Ajouter un membre")
        print("[2] Retirer un membre")
        print("[3] Afficher la flotte")
        print("[4] Vérifier un vaisseau")
        print("[5] Ajouter un vaisseau")
        print("[6] Statistiques de la flotte")
        print("[7] Sauvegarder la flotte")
        print("[8] Charger une flotte")
        print("[0] Quitter")
        try:
            choix = int(input("Votre choix : "))
            match choix:
                case 1:
                    add_crew_member(fleet)
                    break
                case 2: 
                    remove_crew_member(fleet)
                    break
                case 3: 
                    display_fleet(fleet)
                    break
                case 4:
                    check_spaceship(fleet)
                    break
                case 5:
                    add_spaceship(fleet)
                    break
                case 6:
                    fleet.statistics()
                    break
                case 7:
                    save_menu(fleet)
                    break
                case 8:
                    fleet = load_menu(fleet)
                    break
                case 0: 
                    quitter()
                    break
                case _:
                    print("Veuillez entrer un chiffre valide")
        except ValueError as erreur:
            print(f"Erreur : {erreur}")
            
while True:
    menu()
            
            
        