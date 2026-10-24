from person import Operator, Mentalist, ROLES
from spaceship import Spaceship
from fleet import Fleet

#TP1

def add_member(crew):
    new_crew = {"first_name": "", "last_name": "", "gender": "", "age": 0, "role": ""}
    MIN_LENGTH = 3 
    MAX_LENGTH = 15
    while True:
        new_crew["first_name"] = str(input("Votre prénom : "))
        if len(new_crew["first_name"]) <= MIN_LENGTH or  len(new_crew["first_name"]) >= MAX_LENGTH:
            print(f"Votre prénom {new_crew['first_name']} doit faire entre 3 et 15 caractères")
            continue
        else :
            print(f"Votre prénom {new_crew['first_name']} a bien été enregistrer")
            
        while True:
            new_crew["last_name"] = input("Votre nom : ")

            if len(new_crew["last_name"].lower()) < MIN_LENGTH or len(new_crew["last_name"].lower()) > MAX_LENGTH:
                print(f"Votre nom {new_crew["last_name"]} doit faire entre {MIN_LENGTH} et {MAX_LENGTH} caractères")
            elif any(new_crew["last_name"].lower() == i["last_name"].lower() for i in crew):
                print(f"Votre nom {new_crew["last_name"]} existe déjà")
            else:
                new_crew["last_name"] = new_crew["last_name"]
                print(f"Votre nom {new_crew["last_name"]} a bien été enregistré")
                break
        
        new_crew["gender"] = str(input("Votre genre (F ou M) : "))
        if new_crew["gender"] not in ("F", "M"):
            print(f"Votre genre {new_crew['gender']} doit être soit F soit M")
            continue
        else : 
            print(f"Votre genre {new_crew['gender']} a bien été enregistrer")
        
        try :
            new_crew["age"] = int(input("Votre âge : "))
        except ValueError:
            print(f"Votre age doit être un int")
            continue
        else :
            print(f"Votre age {new_crew['age']} a bien été enregistrer")
            
        new_crew["role"] = str(input("Votre rôle : "))
        if new_crew["role"] not in ("commandant", "pilote", "technicien", "armurier", "marchand", "entretien"):
            print(f"Veuillez saisir un rôle parmi cette liste {ROLES} ! ")
            continue
        else : 
            print(f"Votre rôle {new_crew['role']} a bien été enregistrer ! ")
        crew.append(new_crew)
        print(crew)
        return crew


def remove_member(crew):
    while True:
        compteur = 0
        delete_crew = input("Veuillez entrer un nom pour supprimer la totalité des informations : ")
        for i in range(len(crew)):
            if crew[i]["last_name"] == delete_crew:
                compteur += 1
                del crew[i]
                print(f"Le membre {delete_crew} a bien été supprimé ! ")
                break
            else : 
                print(f"le membre {delete_crew} n'existe pas !")
        print(crew)
        return crew

def display_crew(crew):
    compteur = 0
    for i in crew:
        compteur += 1
        print(f"{compteur}. Prénom : {i['first_name']}, Nom : {i['last_name']}, "
              f"Genre : {i['gender']}, Age : {i['age']}, Rôle : {i['role']}")
    if compteur == 0:
        print("Aucun membre n'est disponible")
    return

def check_crew(crew):
    pilote = False
    technicien = False

    for membre in crew:
        if membre["role"] == "pilote":
            pilote = True
        if membre["role"] == "technicien":
            technicien = True

    if len(crew) >= 2 and pilote and technicien:
        print("L'équipage est prêt pour la mission !")
        return True

    print("L'équipage n'est pas prêt, il manque :")
    if len(crew) < 2:
        print("au moins 2 membres")
    if not pilote:
        print("un pilote")
    if not technicien:
        print("un technicien")
    return False

def quitter():
    print("Au revoir ! ")
    exit()
    return

def build_fleet(data):
    fleet = Fleet(data["name"])

    for ship_data in data["spaceships"]:
        ship = Spaceship(ship_data["name"], ship_data["ship_type"], ship_data["condition"])

        for member_data in ship_data["crew"]:
            first_name = member_data["first_name"]
            last_name = member_data["last_name"]
            gender = member_data["gender"]
            age = member_data["age"]

            if member_data["type"] == "operator":
                member = Operator(first_name, last_name, gender, age, member_data["role"])
            elif member_data["type"] == "mentalist":
                member = Mentalist(first_name, last_name, gender, age, member_data["mana"])

            ship.add_member(member)

        fleet.add_spaceship(ship)

    return fleet


#TP2
def ask_spaceship(fleet):
    name = input("Nom du vaisseau : ")
    ship = fleet.find_spaceship(name)
    if ship is None:
        print(f"Le vaisseau {name} n'existe pas !")
    return ship


def add_crew_member(fleet):
    ship = ask_spaceship(fleet)
    if ship is None:
        return

    MIN_LENGTH = 3
    MAX_LENGTH = 15
    while True:
        kind = input("Opérateur ou mentaliste (o/m) : ")
        if kind not in ("o", "m"):
            print("Tapez o pour opérateur ou m pour mentaliste")
            continue

        first_name = input("Votre prénom : ")
        if len(first_name) < MIN_LENGTH or len(first_name) > MAX_LENGTH:
            print(f"Votre prénom {first_name} doit faire entre {MIN_LENGTH} et {MAX_LENGTH} caractères")
            continue
        print(f"Votre prénom {first_name} a bien été enregistré")

        while True:
            last_name = input("Votre nom (vide si aucun) : ")
            if last_name != "" and (len(last_name) < MIN_LENGTH or len(last_name) > MAX_LENGTH):
                print(f"Votre nom {last_name} doit faire entre {MIN_LENGTH} et {MAX_LENGTH} caractères")
            elif ship.find_member(last_name or first_name) is not None:
                print(f"Votre nom {last_name or first_name} existe déjà sur {ship.name}")
            else:
                print(f"Votre nom {last_name} a bien été enregistré")
                break

        gender = input("Votre genre (F ou M) : ")
        if gender not in ("F", "M"):
            print(f"Votre genre {gender} doit être soit F soit M")
            continue
        print(f"Votre genre {gender} a bien été enregistré")

        try:
            age = int(input("Votre âge : "))
        except ValueError:
            print("Votre âge doit être un nombre")
            continue
        print(f"Votre âge {age} a bien été enregistré")

        if kind == "o":
            role = input("Votre rôle : ")
            if role not in ROLES:
                print(f"Veuillez saisir un rôle parmi cette liste {ROLES} ! ")
                continue
            print(f"Votre rôle {role} a bien été enregistré ! ")
            member = Operator(first_name, last_name, gender, age, role)
        else:
            member = Mentalist(first_name, last_name, gender, age)

        ship.add_member(member)          
        print(f"{member.name} a bien été ajouté à {ship.name} !")
        return


def remove_crew_member(fleet):
    ship = ask_spaceship(fleet)
    if ship is None:
        return

    compteur = 0
    delete_crew = input("Veuillez entrer un nom pour supprimer la totalité des informations : ")
    for i in range(len(ship.crew)):
        member = ship.crew[i]
        if (member.last_name or member.first_name) == delete_crew:
            compteur += 1
            del ship.crew[i]
            print(f"Le membre {delete_crew} a bien été supprimé ! ")
            break

    if compteur == 0:
        print(f"Le membre {delete_crew} n'existe pas !")


def display_fleet(fleet):
    if len(fleet.spaceships) == 0:
        print("Aucun vaisseau n'est disponible")
    for ship in fleet.spaceships:
        print(ship)
        compteur = 0
        for member in ship.crew:
            compteur += 1
            if isinstance(member, Operator):
                role = member.role
            else:
                role = "mentaliste"
            print(f"{compteur}. Prénom : {member.first_name}, Nom : {member.last_name}, "
                  f"Genre : {member.gender}, Age : {member.age}, Rôle : {role}")
        if compteur == 0:
            print("Aucun membre n'est disponible")


def check_spaceship(fleet):
    ship = ask_spaceship(fleet)
    if ship is None:
        return False

    pilote = False
    technicien = False
    for member in ship.crew:
        if isinstance(member, Operator):     
            if member.role == "pilote":
                pilote = True
            if member.role == "technicien":
                technicien = True

    if pilote and technicien:
        print(f"{ship.name} est prêt pour la mission !")
        return True

    print(f"{ship.name} n'est pas prêt, il manque :")
    if not pilote:
        print("un pilote")
    if not technicien:
        print("un technicien")
    return False


def add_spaceship(fleet):
    name = input("Nom du vaisseau : ")
    ship_type = input("Type (transport, guerre ou marchand) : ")
    if ship_type not in ("transport", "guerre", "marchand"):
        print("Le type doit être transport, guerre ou marchand")
        return

    fleet.add_spaceship(Spaceship(name, ship_type))   
    print(f"Le vaisseau {name} a bien été ajouté !")