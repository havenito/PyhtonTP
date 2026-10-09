line = " Failed password for root from 10.0.0.5 "

line = line.strip() # retire les espaces
words = line.split(" ") # liste de mots
user, ip = words[3], words[-1]

print(line.startswith("Failed")) # True
print(user.upper()) # ROOT
print(f"Échec pour {user} depuis {ip}")
print(f"CVSS : {9.8123:.1f}") # CVSS : 9.8