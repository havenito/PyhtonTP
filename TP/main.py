from crew import *

crew = [
{"first_name": "Bel", "last_name": "Riose", "gender": "M", "age": 48, "role": "commandant"},
{"first_name": "Gaal", "last_name": "Dornick", "gender": "F", "age": 34, "role": "technicien"},
{"first_name": "Hugo", "last_name": "Crast", "gender": "M", "age": 37, "role": "pilote"},
{"first_name": "Salvor", "last_name": "Hardin", "gender": "F", "age": 28, "role": "armurier"},
{"first_name": "Novi", "last_name": "Sura", "gender": "F", "age": 25, "role": "entretien"},
]

def menu():
    while True:
        print("===== Flotte marchande - Gestion de l'équipage =====")
        print("[1] Ajouter un membre")
        print("[2] Retirer un membre")
        print("[3] Afficher l'équipage")
        print("[4] Vérifier l'équipage")
        print("[0] Quitter")
        choix = int(input("Votre choix : "))
        match choix:
            case 1:
                add_member(crew)
                break
            case 2: 
                remove_member()
                break
            case 3: 
                display_crew()
                break
            case 4:
                check_crew()
                break
            case 0: 
                quitter()
                break
            case _:
                print("Veuillez entrer un chiffre valide")
            
while True:
    menu()
            
            
        