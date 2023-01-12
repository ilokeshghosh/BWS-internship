# input Charmander for example

import requests

while True:
    pokemon = input("Name of the pokemon to see details : ")
    pokemon = pokemon.lower()

    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"

    req = requests.get(url)
    if req.status_code == 200:
        data = req.json()
        print(f"Name is\t\t : {data['name']}")
        print("Abilities:")
        for ability in data['abilities']:
            print(ability['ability']['name'])
    else:
        print("Sorry Data not found")