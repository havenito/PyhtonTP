def is_valid_port(port):
    """Vrai si port est un port TCP valide."""
    return 0 <= port <= 65535

def format_alert(ip, level="INFO"):
    return f"[{level}] Activité suspecte : {ip}"

print(is_valid_port(8080)) # True
print(is_valid_port(70000)) # False
print(format_alert("10.0.0.5")) # [INFO] …
print(format_alert("10.0.0.5", "HIGH")) # [HIGH] Activité suspecte : 10.0.0.5