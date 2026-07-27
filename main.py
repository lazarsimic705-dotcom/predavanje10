
import json  #importovanje data.json u main


with open("data.json", "r") as file:  #ucitaj data.json, R-citanje fajla
    data = json.load(file)           # ucitaj podatke iz json fajla
    data.append({
        "nama": "Lazar Nikolic",
        "age": 22,
        "height": 195,
        "gander": "male"
    })


print(data)

# W - write,  R - Read
with open("data.json", "w") as file:
    json.dump(data, file, indent=4)        # IDENT=4 - lepse pisanje i odvajanje fafla od fajla



