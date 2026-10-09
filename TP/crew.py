ROLES = ["commandant", "pilote", "technicien", "armurier", "marchand", "entretien"]


def add_member(crew):
    new_crew = {"first_name": "", "last_name": "", "gender": "", "age": 0, "role": ""}
    MIN_LENGTH = 3 
    MAX_LENGTH = 15
    F = "F"
    M = "M"
    while True:
        new_crew["first_name"] = str(input("Votre prénom : "))
        if len(new_crew["first_name"]) <= MIN_LENGTH or  len(new_crew["first_name"]) >= MAX_LENGTH:
            print(f"Votre prénom {new_crew['first_name']} doit faire entre 3 et 15 caractères")
            continue
        else :
            print(f"Votre prénom {new_crew['first_name']} a bien été enregistrer")
            
        new_crew["last_name"] = str(input("Votre nom : "))
        if len(new_crew["last_name"]) <= MIN_LENGTH or  len(new_crew["last_name"]) >= MAX_LENGTH:
            print(f"Votre nom {new_crew['last_name']} doit faire entre 3 et 15 caractères")
        else :
            for i in crew:
                if new_crew["last_name"] == i["last_name"]:
                    print(f"Votre nom {new_crew['last_name']} existe déjà")
                    continue
            print(f"Votre nom {new_crew['last_name']} a bien été enregistrer")
        
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
        return crew


def remove_member(crew):
    return

def display_crew(crew): 
    return

def check_crew(crew): 
    return 

def quitter(crew):
    print("Au revoir ! ")
    exit(0)
    return