ROLES = ["commandant", "pilote", "technicien", "armurier", "marchand", "entretien"]

ACTIONS = {
    "commandant": "donne ses ordres à l'équipage",
    "pilote": "pilote le vaisseau",
    "technicien": "répare les moteurs",
    "armurier": "vérifie les canons",
    "marchand": "négocie une cargaison",
    "entretien": "nettoie le vaisseau",
}

class Person:
    def __init__(self, first_name, last_name, gender, age):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.age = age
        self.introduce_yourself()
        
    def introduce_yourself(self):
        print(f"Je m'appelle {self.first_name} {self.last_name}, je suis un {self.gender} de {self.age} ans.")
        if not self.last_name:
            print("")
        
    def __str__(self):
        return f"{self.first_name} {self.last_name}, ({self.gender}, {self.age})"

        
        
        
    
