#En la rama Develop se harán los cambios y la implementación del Pokedex

"""Uso las librerias request para realizar busquedas en internet 
y json para guardar los datos del pokemons en una archivo json"""
import json
import requests


# Estas dos primeras funciones podemos volverla uno sola
#  que piensas solo cambiando la clave a usar en la api del URI

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


def cargar_base_de_datos(file_path):
    """ Carga la base de datos y almacena esos datos"""
    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_from_json(data,file_path):
    """funcion para guardar los datos en un pokedex personal"""

    with open(file_path,  "w") as file:
        json.dump(data, file, indent=2)

def menu_principal():
    while True:
        print("\nMenú Principal:")
        print("1. Obtener información de un Pokémon")
        print("2. Actualizar información de un Pokémon")
        print("3. Crear un nuevo Pokémon")
        print("4. Eliminar un Pokémon")
        print("5. Salir")
        
        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            # Interacción con el usuario
            busqueda = input("\nIngrese el nombre o número de la Pokédex del Pokémon que desea buscar: ")

            # Llamar a la función de solicitud
            if busqueda.isnumeric():
                pokemon = obtener_informacion_pokemon_por_numero(busqueda)
            else:
                pokemon = obtener_informacion_pokemon(busqueda.lower())

            # Procesar y mostrar los resultados
            if pokemon:
                print("\nInformación del Pokémon:")
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
                base_de_datos = cargar_base_de_datos("pokedex_usuario.json")
                base_de_datos.append(datos_pokemon)
                save_from_json(base_de_datos, "pokedex_usuario.json")

                print("\nEl Pokémon se ha guardado en el archivo la Pokedex del usuario.")

        elif opcion == "2":
           
            # Interacción con el usuario
            busqueda = input("\nIngrese el nombre o número de la Pokédex del Pokémon que desea actualizar: ")

            nuevos_datos = {}

            # Solicitar información al usuario
            nuevos_datos["height"] = int(input("Ingrese la nueva altura del Pokémon: "))
            nuevos_datos["weight"] = int(input("Ingrese el nuevo peso del Pokémon: "))
            tipos = input("Ingrese los tipos del Pokémon separados por comas: ")
            nuevos_datos["types"] = [{"type": {"name": tipo.strip()}} for tipo in tipos.split(",")]

            pokemon_actualizado = actualizar_informacion_pokemon(busqueda, nuevos_datos)
            if pokemon_actualizado:
                print("Información actualizada del Pokémon:")
                print(f"Nombre: {pokemon_actualizado['name']}")
                print(f"Altura: {pokemon_actualizado['height']} cm")
                print(f"Peso: {pokemon_actualizado['weight']} kg")

            # Guardar el Pokémon en un archivo JSON u obtener información desde la API

                # Verificar si algún valor en los datos es None
                if None in pokemon_actualizado.values():
                    print("La API devolvió datos nulos. No se guardarán en la base de datos.")
                else:
                    # Guardar los datos en la base de datos local JSON

                    base_de_datos = cargar_base_de_datos("pokedex_usuario.json")
                    base_de_datos.append(pokemon_actualizado)
                    save_from_json(base_de_datos, "pokedex_usuario.json")

                    print("El Pokémon se ha guardado en el archivo la Pokedex del usuario.")
            else:
                print("No se pudo obtener la información del Pokémon desde la API.")

        elif opcion == "3":
            nuevo_pokemon = {}

            # Solicitar información al usuario
            nuevo_pokemon ["name"] = input("Ingrese el nombre del Pokémon: ")
            nuevo_pokemon ["height"] = int(input("Ingrese la altura del Pokémon: "))
            nuevo_pokemon ["weight"] = int(input("Ingrese el peso del Pokémon: "))
            tipos = input("Ingrese los tipos del Pokémon separados por comas: ")
            nuevo_pokemon ["types"] = [{"type": {"name": tipo.strip()}} for tipo in tipos.split(",")]

            nuevo_pokemon_creado = crear_nuevo_pokemon(nuevo_pokemon)
            if nuevo_pokemon_creado:
                print("Nuevo Pokémon creado:")
                print(f"Nombre: {nuevo_pokemon_creado['name']}")
                print(f"Altura: {nuevo_pokemon_creado['height']} cm")
                print(f"Peso: {nuevo_pokemon_creado['weight']} kg")

            # Guardar el Pokémon en un archivo JSON u obtener información desde la API

                # Verificar si algún valor en los datos es None
                if None in nuevo_pokemon_creado.values():
                    print("La API devolvió datos nulos. No se guardarán en la base de datos.")
                else:
                    # Guardar los datos en la base de datos local JSON

                    base_de_datos = cargar_base_de_datos("pokedex_usuario.json")
                    base_de_datos.append(nuevo_pokemon_creado)
                    save_from_json(base_de_datos, "pokedex_usuario.json")

                    print("El Pokémon se ha guardado en el archivo la Pokedex del usuario.")
            else:
                print("No se pudo obtener la información del Pokémon desde la API.")

        elif opcion == "4":
            busqueda = input("\nIngrese el nombre o número de la Pokédex del Pokémon que desea eliminar: ")
            eliminar_pokemon(busqueda)

        elif opcion == "5":
            print("\nSaliendo del programa.")
            break
        
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

# Llamar a la función principal del menú
menu_principal()


"""
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

    """