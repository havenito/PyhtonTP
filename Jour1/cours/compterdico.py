log = [
"Failed password for root from 10.0.0.5",
"Accepted password for Chris from 10.0.0.9",
"Failed password for admin from 10.0.0.5",
]
failures = {}
for line in log:
    if line.startswith("Failed"):
        ip = line.split(" ")[-1]
        failures[ip] = failures.get(ip, 0) + 1
print(failures) # {'10.0.0.5': 2}