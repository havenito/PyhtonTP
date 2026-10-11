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
            sexe = "un homme"
        else:
            sexe = "une femme"
        return f"Je m'appelle {self.name}, je suis {sexe} de {self.age} ans."
        
    def __str__(self):
        return f"{self.name} ({self.gender}, {self.age} ans)"
    
class Operator(Person):
    def __init__(self, first_name, last_name, gender, age, role):
        super().__init__(first_name, last_name, gender, age)
        self.role = role
        self._experience = 0

    @property
    def role(self):
        return self._role

    @role.setter
    def role(self, value):
        if value not in ROLES:
            raise ValueError(f"Rôle inconnu : {value}. Rôles valides : {ROLES}")
        self._role = value

    @property
    def experience(self):
        return self._experience

    def gain_experience(self):
        self._experience += 1

    def act(self):
        print(f"{self.name} {ACTIONS[self.role]}")
        self.gain_experience()

    def __str__(self):
        return f"{super().__str__()} {self.role}"