ROLES = ["commandant", "pilote", "technicien", "armurier", "marchand", "entretien"]


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