
import requests
import json
import csv


response = requests.get("http://api.nbp.pl/api/exchangerates/tables/C?format=json")
data = response.json()
data_as_json = json.dumps(data)
data_from_json = json.loads(data_as_json)
rates = data_from_json[0]["rates"]

with open("obsluga_api.csv", "w", newline="") as f:
    writer = csv.writer(f, delimiter=';')
    writer.writerow(dict.keys(rates[0]))
    for i in rates:
        writer.writerow(dict.values(i))