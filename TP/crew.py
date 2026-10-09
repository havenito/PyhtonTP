ROLES = ["commandant", "pilote", "technicien", "armurier", "marchand", "entretien"]


def add_member(crew): 
    crew = []
    MIN_LENGTH = 3 
    MAX_LENGTH = 15
    while True:
        prenom_input = str(input("Votre prénom : "))
        if len(crew) >= MIN_LENGTH and  len(crew) >= MAX_LENGTH:
            print(f"Votre prénom {prenom_input} a bien été enregistré")
            break
        else :
            print(f"Votre prénom {prenom_input} doit faire entre 3 et 15 caractères")
        return


def remove_member(crew):
    return

def display_crew(crew): 
    return

def check_crew(crew): 
    return 

def quitter(crew):
    return