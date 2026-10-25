from person import Operator, Mentalist, ROLES


class Fleet:

    MAX_SPACESHIPS = 15             

    def __init__(self, name):
        self.name = name
        self.spaceships = []    
    
    def to_dict(self):
        spaceships = []
        for spaceship in self.spaceships:
            spaceships.append(spaceship.to_dict())
        return {
            "name": self.name,
            "spaceships": spaceships
        }      

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

        for spaceship in self.spaceships:
            if spaceship.check_preparation():
                ready += 1
            for member in spaceship.crew:
                members += 1
                if isinstance(member, Operator):
                    operators += 1
                    total_experience += member.experience
                    if member.role in roles:
                        roles[member.role] += 1
                    else:
                        roles[member.role] = 1
                elif isinstance(member, Mentalist):
                    mentalists += 1

        if operators > 0:
            average = total_experience / operators
        else:
            average = 0.0

        print(f"Flotte {self.name} : {len(self.spaceships)} vaisseaux, {members} membres")
        for role in roles:
            print(f"{role} : {roles[role]}")
        print(f"mentaliste : {mentalists}")
        print(f"Expérience moyenne des opérateurs : {average:.1f}")
        print(f"Vaisseaux prêts : {ready} / {len(self.spaceships)}")