COMMON_PASSWORDS = [
    "123456", "password", "azerty", "qwerty", "motdepasse",
    "admin", "letmein", "iloveyou", "000000", "azertyuiop",
    "Password123!", "Azerty123456!",
]

def check_password(password, is_admin=False):
    error = []
    normalized_password = password.strip().lower()
    for i in range(len(password)):
        if len(password) < 12 and not is_admin:
            error.append("Le mot de passe doit contenir 12 caractères")
        if len(password) < 16 and is_admin:
            error.append("Le mot de passe doit contenir 16 caractères")
        if not password[i].isupper():
            password[i].isupper() == False
            error.append("Le mot de passe doit contenir une majuscule")
        if not any(i.islower() for i in password):
            password[i].islower() == False
            error.append("Le mot de passe doit contenir une minuscule")
        if not any(char.isdigit() for char in password):
            password[i].isdigit() == False
            error.append("Le mot de passe doit contenir un chiffre")
        if not password[i].isalnum():
            password[i].isalnum() == False
            error.append("Le mot de passe doit contenir un caractère alphanumérique")
        if normalized_password in [reserved.lower() for reserved in COMMON_PASSWORDS]:
            error.append ("Le mot de passe ne doit pas être courant")
        result = (True, error) if not error else (False, error)
        return result

print(check_password("Tr0ub4dour&Co"))
# (True, [])
print(check_password("Azerty123456!"))
# (False, ['ne doit pas être un mot de passe courant'])
print(check_password("azerty"))
# (False, ['au moins 12 caractères', 'au moins une majuscule',
#          'au moins un chiffre', 'au moins un caractère spécial',
#          'ne doit pas être un mot de passe courant'])
print(check_password("correcthorse battery staple"))
# (False, ['au moins une majuscule', 'au moins un chiffre'])
print(check_password("Tr0ub4dour&Co", is_admin=True))
# (False, ['au moins 16 caractères']
print(check_password("Test1234333333333333."))