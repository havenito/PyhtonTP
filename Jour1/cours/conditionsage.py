username = input("Votre nom d'user :")
age = input("Votre age :")

if age > 18:
    print("Vous êtes majeur")
elif age >= 18 and age < 60:
    print("Vous êtes adulte")
elif age >= 60:
    print("Vous êtes senior")
elif age >= 0 and age < 18:
    print("Vous êtes mineur")
else:
    print("Age invalide")