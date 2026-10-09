role = "analyst"
failed_attempts = 1
if failed_attempts >= 3:
    print("Compte verrouillé")
elif role == "admin":
    print("Accès total")
elif role == "analyst":
    print("Accès en lecture") # ← exécuté
else:
    print("Accès refusé")
    
