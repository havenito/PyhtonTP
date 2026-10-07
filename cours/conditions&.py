password_ok = True
mfa_ok = False
blocked_ips = ["10.0.0.5", "203.0.113.7"]
ip = "10.0.0.5"
if password_ok and mfa_ok:
    print("Connexion autorisée")
if not mfa_ok:
    print("Code MFA manquant") # ← exécuté
if ip in blocked_ips or ip.startswith("192.0.2."):
    print(f"{ip} est bloquée") # ← exécuté