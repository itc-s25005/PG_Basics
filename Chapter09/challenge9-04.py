import csv

movies=[
        ["トップガン", "卒業白書", "マイノリティ・リポート"],
        ["タイタニック", "レヴェナント", "インセプション"],
        ["トレーニングデイ", "マイ・ボディガード", "フライト"]
]

with open ("movie2.sv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    for item in movies:
        writer.writerow(item)
