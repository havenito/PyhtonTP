# Tuple : non modifiable
target = ("10.0.0.5", 22)
ip, port = target # déballage
print(f"{ip}:{port}") # 10.0.0.5:22
# Ensemble : valeurs uniques, sans ordre
ips = ["10.0.0.5", "10.0.0.9", "10.0.0.5"]
unique_ips = set(ips)           #Sans doublon et sans ordre : parfait pour dédupliquer les IP d'un journal
print(len(unique_ips)) # 2
unique_ips.add("10.0.0.12")
print("10.0.0.9" in unique_ips) # True