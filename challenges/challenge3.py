import string
import secrets

def generate_password(lenght=16):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    while True:
        password = ''.join(secrets.choice(alphabet) for i in range(lenght))
        #password = "Testmdp12!"
        if len(password) < 12:
                raise ValueError("Le mot de passe doit faire au moins 12 caractères.")
        if (any(c.islower() for c in password)
                and any(c.isupper() for c in password)
                and any(c.isdigit() for c in password)):
            break
    return password

print(generate_password())