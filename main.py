
import json  #importovanje user.json u main


with open("data/user.json", "r") as file:  #ucitaj user.json, R-citanje fajla
    data = json.load(file)           # ucitaj podatke iz json fajla
    data.append({
        "nama": "Lazar Nikolic",
        "age": 22,
        "height": 195,
        "gander": "male"
    })


print(data)

# W - write,  R - Read
with open("data/user.json", "w") as file:
    json.dump(data, file, indent=4)        # IDENT=4 - lepse pisanje i odvajanje fafla od fajla



