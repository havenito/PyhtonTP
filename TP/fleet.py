from person import Operator, Mentalist, ROLES


class Fleet:

    MAX_SPACESHIPS = 15             

    def __init__(self, name):
        self.name = name
        self.spaceships = []          

    def add_spaceship(self, spaceship):
        if len(self.spaceships) >= Fleet.MAX_SPACESHIPS:
            raise ValueError("capacité maximale atteinte")
        if self.find_spaceship(spaceship.name) is not None:
            raise ValueError(f"{spaceship.name} fait déjà partie de la flotte")
        self.spaceships.append(spaceship)

    def find_spaceship(self, name):
        for spaceship in self.spaceships:
            if spaceship.name.lower() == name.lower():  
                return spaceship
        return None

    def statistics(self):
        members = 0
        mentalists = 0
        operators = 0
        total_experience = 0
        ready = 0
        roles = {}
        for role in ROLES:
            roles[role] = 0

        for spaceship in self.spaceships:
            if spaceship.check_preparation():
                ready += 1
            for member in spaceship.crew:
                members += 1
                if isinstance(member, Operator):
                    operators += 1
                    total_experience += member.experience
                    roles[member.role] += 1
                elif isinstance(member, Mentalist):
                    mentalists += 1

        if operators > 0:
            average = total_experience / operators
        else:
            average = 0
            
        print(f"Flotte {self.name}")
        print(f"Vaisseaux : {len(self.spaceships)}")
        print(f"Membres : {members}")
        print("Répartition par rôle :")
        for role in ROLES:
            print(f"  {role} : {roles[role]}")
        print(f"Mentalistes : {mentalists}")
        print(f"Expérience moyenne des opérateurs : {average:.1f}")
        print(f"Vaisseaux prêts : {ready}")