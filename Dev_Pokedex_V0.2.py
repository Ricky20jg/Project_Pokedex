#En la rama Develop se harán los cambios y la implementación del Pokedex

"""Uso las librerias request para realizar busquedas en internet 
y json para guardar los datos del pokemons en una archivo json"""
import json
from mod_pokedex import functions_pokedex
# Estas dos primeras funciones podemos volverla uno sola
#   solo cambiando la clave a usar en el URI del API

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
                pokemon = functions_pokedex.obtener_informacion_pokemon_por_numero(busqueda)
            else:
                pokemon = functions_pokedex.obtener_informacion_pokemon(busqueda.lower())

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

            pokemon_actualizado = functions_pokedex.actualizar_informacion_pokemon(busqueda, nuevos_datos)
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

            nuevo_pokemon_creado = functions_pokedex.crear_nuevo_pokemon(nuevo_pokemon)
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
            functions_pokedex.eliminar_pokemon(busqueda)

        elif opcion == "5":
            print("\nSaliendo del programa.")
            break

        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

# Llamar a la función principal del menú
menu_principal()
