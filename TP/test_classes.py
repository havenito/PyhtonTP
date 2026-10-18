from person import Operator, Mentalist
from spaceship import Spaceship

bel = Operator("Bel", "Riose", "M", 48, "commandant")
hugo = Operator("Hugo", "Crast", "M", 37, "pilote")
joie = Mentalist("Joie", "", "F", 25)

print(bel.introduce_yourself())   # Je m'appelle Bel Riose, je suis un homme de 48 ans.
print(joie.introduce_yourself())  # Je m'appelle Joie, je suis une femme de 25 ans.
print(hugo)                       # Hugo Crast (M, 37 ans) – pilote
print(joie)                       # Joie (F, 25 ans) – mentaliste, 100 mana

hugo.act()                        # Hugo Crast pilote le vaisseau.
print(hugo.experience)            # 1

for _ in range(6):
    joie.influence(hugo)          # 5 fois : Joie influence Hugo Crast. (puis Hugo agit)
                                  # 6e fois : Joie n'a pas assez de mana…
print(joie.mana)                  # 0
joie.recharge_mana()
joie.recharge_mana()
joie.recharge_mana()
print(joie.mana)                  # 100 : le mana ne dépasse jamais 100

ship = Spaceship("Fearless", "guerre")
ship.add_member(bel)
ship.add_member(hugo)
print(ship.check_preparation())   # False : pas de technicien
ship.add_member(Operator("Yugo", "Amary", "M", 33, "technicien"))
print(ship.check_preparation())   # True
print(ship)                       # Fearless (guerre, opérationnel) – 3 membres

Operator("Eve", "Hacker", "F", 30, "root")
# ValueError: rôle inconnu : root
