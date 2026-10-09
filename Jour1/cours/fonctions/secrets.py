import secrets
import string

token = secrets.token_hex(16) # jeton
print(token) # 32 caractères au hasard

c = secrets.choice(string.ascii_letters)
print(c) # une lettre au hasard