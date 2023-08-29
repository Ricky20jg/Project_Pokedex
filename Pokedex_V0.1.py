#En la rama Develop se hará la implementación del Pokedex

"""Uso las librerias request para realizar busquedas en internet 
y json para guardar los datos del pokemons en una archivo json"""
import json
import requests

def obtener_informacion_pokemon(nombre):
    """busco al pokemon en la pokedex por su nombre"""

    url = f"https://pokeapi.co/api/v2/pokemon/{nombre}"
    respuesta = requests.get(url, timeout=15)

    if respuesta.status_code == 200:
        busqueda_pokemon = respuesta.json()
        return busqueda_pokemon
    else:
        print("No se pudo obtener la información del Pokémon.")
        return None

def obtener_informacion_pokemon_por_numero(numero):
    """busco al pokemon en la pokedex por su nombre"""

    url = f"https://pokeapi.co/api/v2/pokemon/{numero}"
    respuesta = requests.get(url, timeout=15)

    if respuesta.status_code == 200:
        busqueda_pokemon = respuesta.json()
        return busqueda_pokemon
    else:
        print("No se pudo obtener la información del Pokémon.")
        return None

def save_from_json(data,file_path):
    """funcion para guardar los datos en un pokedex personal"""

    with open(file_path,  "w") as file:
        json.dump(data, file, indent=2)

# Interacción con el usuario
busqueda = input("Ingrese el nombre o número de la Pokédex del Pokémon que desea buscar: ")

# Llamar a la función de solicitud
if busqueda.isnumeric():
    pokemon = obtener_informacion_pokemon_por_numero(busqueda)
else:
    pokemon = obtener_informacion_pokemon(busqueda.lower())

# Procesar y mostrar los resultados
if pokemon:
    print("Información del Pokémon:")
    print(f"Nombre: {pokemon['name']}")
    print(f"Altura: {pokemon['height']} cm")
    print(f"Peso: {pokemon['weight']} kg")
    # Obtener los tipos de Pokémon
    tipos = []
    for tipo in pokemon['types']:
        tipos.append(tipo['type']['name'])

    # Imprimir los tipos de Pokémon
    dos_tipos = ", ".join(tipos)
    print(f"Tipos: {dos_tipos}")

    datos_pokemon = {
        "Nombre": pokemon['name'],
        "Altura": pokemon['height'],
        "Peso": pokemon['weight'],
        "Tipos": [tipo['type']['name'] for tipo in pokemon['types']]
    }

    # Guardar el Pokémon en un archivo JSON
    save_from_json(datos_pokemon, "pokedex_usuario.json")

    print("El Pokémon se ha guardado en el archivo la Pokedex del usuario.")