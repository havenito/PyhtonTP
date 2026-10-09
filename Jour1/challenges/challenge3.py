import string
import secrets
from challenge1 import check_password

def generate_password(lenght=16):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    while True:
        password = ''.join(secrets.choice(alphabet) for i in range(lenght))
        if len(password) < 12:
                raise ValueError("Le mot de passe doit faire au moins 12 caractères.")
        if (any(c.islower() for c in password)
                and any(c.isupper() for c in password)
                and any(c.isdigit() for c in password)
                and any(c in string.punctuation for c in password)):
            break
    return password

if __name__ == "__main__":
    mdp_invalides = 0

    for _ in range(1000):
        mdp = generate_password()
        est_valide, message = check_password(mdp) 
        
        if not est_valide:
            mdp_invalides += 1

    print(f"Mots de passe invalides sur 1000 : {mdp_invalides}")
        

    print(generate_password())
    # par exemple : 45h#O_$APXE[QLje
    print(generate_password(24))
    # par exemple : {U/7/lzny-b{MJb[-B1agCX(
    generate_password(8)
    # ValueError: longueur minimale : 12
    # Vérification avec le défi 1
    # Mots de passe invalides sur 1000 : 0