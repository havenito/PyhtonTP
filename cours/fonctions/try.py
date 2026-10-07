def ask_port():
    while True:
        try:
            port = int(input("Port : "))
        except ValueError:
            print("Entrez un nombre entier.")
        else:
            if 0 <= port <= 65535:
                return port
            raise ValueError("port hors limites")
    
print(f"Scan du port {ask_port()}")