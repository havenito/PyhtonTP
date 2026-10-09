def parse_login(line):
    words = line.split(" ") # locale
    return words[3], words[-1] # un tuple

log = "Failed password for root from 10.0.0.5"
user, ip = parse_login(log)
print(user, ip) # root 10.0.0.5
print(words) # erreur !