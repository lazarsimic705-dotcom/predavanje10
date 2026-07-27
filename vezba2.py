# load_file > file_name

#import json



#def load_file(file_name):
 #   with open(file_name, "r") as file:
 #       products = json.load(file)
 #       return products



# iz methods.py ucitaj funkciju load
from methods import load_file

products = load_file("data/products.json")
users = load_file("data/user.json")
print(products, users)