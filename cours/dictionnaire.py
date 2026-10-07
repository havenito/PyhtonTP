user = {"username": "Chris", "role": "analyst",
"mfa": True}
print(user["role"]) # analyst
user["role"] = "admin" # modification
user["last_ip"] = "10.0.0.5" # ajout d'une clé
print(user.get("email")) # None
print(user.get("email", "?")) # ?
print("mfa" in user) # True
print(list(user.keys()))
# ['username', 'role', 'mfa', 'last_ip']