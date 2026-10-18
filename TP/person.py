from ast import operator


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
            raise ValueError(f"rôle inconnu : {value}")
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
        return f"{super().__str__()} - {self.role}"
    
class Mentalist(Person):
    def __init__(self, first_name, last_name, gender, age, mana=100):
        super().__init__(first_name, last_name, gender, age)
        self.mana = mana
        
    @property
    def mana(self):
        return self._mana
    
    @mana.setter
    def mana(self, value):
        if value < 0:
            self._mana = 0
        elif value > 100:
            self._mana = 100
        else:
            self._mana = value
        
    def act(self):
        print (f"{self.name} se concentre.")
        self.mana += 10
    
    def recharge_mana(self):
        self.mana += 50 
    
    def influence(self, operator):
        if self.mana < 20:
            print(f"{self.name} n'a pas assez de mana pour influencer {operator.name}.")
            return False
        self.mana -= 20
        print(f"{self.name} influence {operator.name}.")
        operator.act()
        return True

    def __str__(self):
        return f"{super().__str__()} - mentaliste, {self.mana} mana"
