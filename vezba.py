# napraviti 5 proizvoda unutar products.json i ucitati ih u vezba.py



import json

with open("data/products.json", "r") as file:
    products = json.load(file)
    print(products)