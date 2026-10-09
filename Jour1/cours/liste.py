open_ports = [443, 22, 80]
print(open_ports[0]) # 443
open_ports.append(3306) # ajoute à la fin
open_ports.remove(80) # retire la valeur 80
open_ports.sort() # trie sur place
print(open_ports) # [22, 443, 3306]
print(len(open_ports)) # 3
print(22 in open_ports) # True
print(open_ports[-2:]) # [443, 3306]