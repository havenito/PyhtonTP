open_ports = [22, 80, 443]

for port in open_ports:
    print(f"Port {port} ouvert")

for i in range(1, 4): # 1, 2, 3
    print(f"Tentative {i}")

for i, port in enumerate(open_ports, 1):
    print(i, port) # 1 22 / 2 80 / 3 443

user = {"name": "Chris", "role": "admin"}
for key, value in user.items():
    print(f"{key} = {value}")