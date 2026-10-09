import Jour1.cours.fonctions.importermodule as importermodule
from Jour1.cours.fonctions.importermodule import is_valid_port

print(importermodule.is_valid_port(22)) # True
print(is_valid_port(-1)) # False