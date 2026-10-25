from person import Operator


class Spaceship:
    """Un vaisseau et son équipage."""

    MAX_CREW = 10                     

    def __init__(self, name, ship_type, condition="opérationnel"):
        self.name = name
        self.ship_type = ship_type   
        self.condition = condition    
        self.crew = []              
    
    def to_dict(self):
        crew = []
        for member in self.crew:
            crew.append(member.to_dict())
        return {
            "name": self.name,
            "ship_type": self.ship_type,
            "condition": self.condition,
            "crew": crew
        }

    def _key(self, member):
        if member.last_name != "":
            return member.last_name
        return member.first_name

    def add_member(self, member):
        if len(self.crew) >= Spaceship.MAX_CREW:
            raise ValueError("capacité maximale atteinte")
        if self.find_member(self._key(member)) is not None:
            raise ValueError(f"{self._key(member)} est déjà à bord")
        self.crew.append(member)

    def find_member(self, name):
        for member in self.crew:
            if self._key(member) == name:
                return member
        return None

    def remove_member(self, name):
        member = self.find_member(name)
        if member != None:
            self.crew.remove(member)
        return member

    def check_preparation(self):
        has_pilot = False
        has_technician = False
        for member in self.crew:
            if isinstance(member, Operator): 
                if member.role == "pilote":
                    has_pilot = True
                if member.role == "technicien":
                    has_technician = True
        return has_pilot and has_technician

    def watch_round(self):
        for member in self.crew:
            member.act()                     

    def __str__(self):
        return f"{self.name} ({self.ship_type}, {self.condition}) – {len(self.crew)} membres"