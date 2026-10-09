SECRET = "S3cur3!"
attempts = 0

while True:
    password = input("Mot de passe : ")
    attempts += 1 # attempts = attempts + 1
    if password == SECRET:
        print("Accès autorisé")
        break # sortie immédiate
    if attempts == 3:
        print("Compte verrouillé")
        break
