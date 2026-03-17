import csv

ips = []

with open("logs.csv", "r") as f:
    reader = csv.reader(f)
    next(reader)  # Skip header

    for row in reader:
        ips.append(row[0])

print(f"IPs: {ips}")