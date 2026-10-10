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
    
    @property
    def name(self):
       return f"{self.first_name} {self.last_name}".strip()
       
    def introduce_yourself(self):
        if self.gender == "M":
            sexe = "homme"
        else:
            sexe = "femme"
        return f"Je m'appelle {self.name}, je suis un {sexe} de {self.age} ans."
        
    def __str__(self):
        return f"{self.name} ({self.gender}, {self.age} ans)"

        
        
    
