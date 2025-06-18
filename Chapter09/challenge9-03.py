import csv

movies=[
        ["Top Gun", "Risky Business", "Minority Report"],
        ["Titanic", "The Revenant", "Inception"],
        ["Training Day", "Man on Fire", "Flight"]
]

with open ("movie.sv", "w", newline="") as f:
    writer = csv.writer(f)
    for item in movies:
        writer.writerow(item)
