from clases import Entrenador, Pokemon, Centro_Pokemon, Tranferencia, Gimnasio
from estructuras import Linked_list_simple, Queue, Stack, HashMap, HashSet
import json, os, time

def borrar():
    input("Presione cualquier tecla para continuar: ")

    

def cargar_pokedex(nombre_archivo): 
    pokedex = HashMap() 
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as archivo: 
            datos = json.load(archivo) 
    except FileNotFoundError: 
        print("No se encontró el archivo") 
        return None 
    
    for p in datos: 
        poke = Pokemon( p["id"], p["nombre"], p["tipo"], p["poder_combate"] ) 
        pokedex.put(poke.id, poke) 
    return pokedex 

def cargar_medallas():
    medallas = HashSet()
    with open("medallas_jugador.json", "r", encoding="utf-8") as archivo:
        datos = json.load(archivo)
    for m in datos:
        medallas.add(m)
    return medallas

def menu_princi():

    entrenador = Entrenador()
    pc = Linked_list_simple()
    curacion = Queue()
    centro = Centro_Pokemon(curacion)
    stack= Stack()
    transferencia= Tranferencia(stack)
    gimnasio= Gimnasio()
    pokedex = cargar_pokedex("pokemones.json")
    medallas= cargar_medallas()


    while True:
        os.system("cls")
        print("=== POKEMON ===")
        print("1. Ver Pokedex")
        print("2. Ver Equipo")
        print("3. Ver PC")
        print("4. Ver Medallas")
        print("5. Capturar Pokemon")
        print("6. Ordenar PC")
        print("7. Buscar Pokemon en Equipo")
        print("8. Enviar Pokemon al Centro Pokemon")
        print("9. Transferir Pokemon al Profesor Oak")
        print("10. Deshacer última transferencia")
        print("11. Desafiar Lider de Gimnasio")
        print("12. Buscar Pokemon por id")
        print("13. Enviar Pokemon del Equipo a la PC")
        print("14. Pasar Pokemon de la PC al Equipo")
        print("15. Salir")

        opcion = input("\nOpción: ")

        if opcion == "1":
            os.system("cls")
            print(pokedex)
            borrar()

        elif opcion == "2":
            os.system("cls")
            entrenador.mostrar_equipo()
            borrar()

        elif opcion == "3":
            os.system("cls")
            if pc.head is None:
                print("No hay pokemones en la pc")
            else:
                pc.mostrar()
                borrar()

        elif opcion == "4":
            os.system("cls")
            print(medallas)
            borrar()

        elif opcion == "5":
            os.system("cls")
            entrenador.atrapar_pokemon(pokedex, pc)
            borrar()

        elif opcion == "6":
            os.system("cls")
            if pc.head is None:
                print("No hay pokemones en la pc")
                borrar()
            else:
                submenu_sorts(pc)
                borrar()

        elif opcion == "7":
            os.system("cls")
            if len(entrenador.equipo) >= 1:
                nombre = input("Nombre del Pokemon: ")
                pokemon = entrenador.buscar_pokemon(nombre)
                if pokemon:
                    print(pokemon)
                else:
                    print("Ese Pokemon no está en el equipo.")
                borrar()
            else:
                print("No hay pokemones en el equipo")
                borrar()

        elif opcion == "8":
            os.system("cls")
            if len(entrenador.equipo) >= 1:

                nombre = input("Nombre del Pokemon a curar: ")
                pokemon = entrenador.buscar_pokemon(nombre)

                if pokemon:
                    centro.ingresar(pokemon)
                    print(f"{pokemon.nombre} ingresó al Centro Pokemon")  
                    opcion2 = input("¿Curarlo ahora? (s/n): ").lower()  
                    if opcion2 == "s":  
                        centro.curar()  
                else:
                    print("Ese Pokemon no está en el equipo.")
                borrar()
            else:
                print("No hay pokemones en tu equipo")
                borrar()

        elif opcion == "9":
            os.system("cls")
            if pc.head is None:
                print("No hay pokemones en la pc")
                borrar()
            else:
                nombre = input("Nombre del Pokemon a transferir: ")
                transferencia.transferir(pc, nombre)
                borrar()

        elif opcion == "10":
            os.system("cls")
            transferencia.deshacer(pc)
            borrar()

        elif opcion == "11":
            os.system("cls")
            if len(entrenador.equipo) < 1:
                print("No puedes desafiar un gimnasio sin pokemones en tu equipo")
                borrar()
            else:
                gimnasio.mostrar_gimnasios()
                try:
                    opcion_gimnasio = int(input("Elegí un gimnasio: "))  
                    gimnasio.desafiar(opcion_gimnasio, medallas)  
                except ValueError: 
                    print("Debe ingresar un número") 
                borrar()

        elif opcion == "12":
            os.system("cls")
            try: 
                id_buscado = int(input("ID del Pokemon: "))  
                pokemon = pokedex.busqueda_binaria(id_buscado)  
                if pokemon: 
                    print("Pokemon encontrado:")
                    print(pokemon)  
                else:  
                    print("Ese ID no existe")

            except ValueError:
                print("Debe ingresar un número") 
            borrar() 
            
        elif opcion == "13":
            os.system("cls")
            if len(entrenador.equipo) < 1:
                print("No hay pokemones en el equipo")
                borrar()
            else:
                nombre = input("Nombre del Pokemon: ")
                entrenador.enviar_a_pc(nombre, pc)
                borrar()
        
        elif opcion == "14":
            os.system("cls")
            if pc.head is None:
                print("No hay pokemones en la pc")
                borrar()
            else:
                os.system("cls")
                entrenador.sacar_de_pc(pc)
                borrar()
        
        elif opcion == "15":
            print("Hasta Luego")
            break

        else:

            print("Opción inválida")
            borrar()
    

def submenu_sorts(pc):
    
    print("1. Ordenar por nombre")
    print("2. Ordenar por tipo")
    print("3. Ordenar por poder de combate")
    
    opcion = input("Opción: ")
    
    if opcion == "1":
        lista = pc.bubble_sort_nombre()

    elif opcion == "2":
        lista = pc.selection_sort_tipo()

    elif opcion == "3":
        lista = pc.quick_sort_pc()
    
    else:
        print("Opción inválida")
        return

    for pokemon in lista:
        print(pokemon)