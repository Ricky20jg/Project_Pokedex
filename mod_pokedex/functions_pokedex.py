#generamos un codigo que 

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

def actualizar_informacion_pokemon(identificador, datos_actualizados):
    """Actualiza la información de un Pokémon en la Pokédex."""

    if identificador.isnumeric():
        url = f"https://pokeapi.co/api/v2/pokemon/{identificador}"
    else:
        url = f"https://pokeapi.co/api/v2/pokemon/{identificador.lower()}"

    respuesta = requests.put(url, json=datos_actualizados, timeout=15)

    if respuesta.status_code == 200:
        pokemon_actualizado = respuesta.json()
        return pokemon_actualizado
    else:
        print("No se pudo actualizar la información del Pokémon.")
        return None

def crear_nuevo_pokemon(datos_pokemon):
    """Crea un nuevo Pokémon en la Pokédex."""

    url = "https://pokeapi.co/api/v2/pokemon"
    respuesta = requests.post(url, json=datos_pokemon, timeout=15)

    if respuesta.status_code == 201:
        nuevo_pokemon = respuesta.json()
        return nuevo_pokemon
    else:
        print("No se pudo crear el nuevo Pokémon.")
        return None

def eliminar_pokemon(identificador):
    """Elimina un Pokémon de la Pokédex."""

    if identificador.isnumeric():
        url = f"https://pokeapi.co/api/v2/pokemon/{identificador}"
    else:
        url = f"https://pokeapi.co/api/v2/pokemon/{identificador.lower()}"

    respuesta = requests.delete(url, timeout=15)

    if respuesta.status_code == 204:
        print("El Pokémon ha sido eliminado correctamente.")
    else:
        print("No se pudo eliminar el Pokémon.")
