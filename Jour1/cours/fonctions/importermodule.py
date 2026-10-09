"""Utilitaires de sécurité."""
def is_valid_port(port):
    return 0 <= port <= 65535

if __name__ == "__main__":
    # si on exécute ce fichier directement
    print(is_valid_port(443))   