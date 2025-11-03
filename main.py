import requests
import json

base_url = "https://pokeapi.co/api/v2/"

def get_pokemon_info(name):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)
    if response.status_code == 200:
        print("Data received!")
        details = response.json()
        return details
    else:
        print(f"Failed to retrieve data {response.status_code}")

pokemon_name = "chimchar"
pokemon_info = get_pokemon_info(pokemon_name)

"""

print(pokemon_info["name"])
print(pokemon_info["height"])
print(pokemon_info["abilities"])

"""
if pokemon_info:
    for ability in pokemon_info["abilities"]:
        json_format = json.dumps(ability)
        print(json_format)
else:
    print(f"Failed to retrieve data about {pokemon_name}!")
