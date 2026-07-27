
#import json  #importovanje user.json u main


#with open("data/user.json", "r") as file:  #ucitaj user.json, R-citanje fajla
 #   data = json.load(file)           # ucitaj podatke iz json fajla
  #  data.append({
  #      "nama": "Lazar Nikolic",
  #      "age": 22,
  #      "height": 195,
   #     "gander": "male"
  #  })

from methods import load_file, save_file

data = load_file("data/user.json")

print(data)

data.append({
    "name": "Test"
})

save_file("data/user.json", data)



# W - write,  R - Read
#with open("data/user.json", "w") as file:
#json.dump(data, file, indent=4)        # IDENT=4 - lepse pisanje i odvajanje fafla od fajla



