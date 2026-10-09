command = "scan"
match command:
    case "scan":
        print("Lancement du scan…") # ← exécuté
    case "report" | "export":           # | => ou
        print("Génération du rapport")
    case "quit":
        print("Au revoir")
    case _:                             #cas par défaut
        print("Commande inconnue")
