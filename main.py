import json
from estructuras import HashSet, HashMap, Nodo, Linked_list_simple, Queue, Stack
from clases import Pokemon, Entrenador, Centro_Pokemon, Tranferencia, Gimnasio
from menus import submenu_sorts

def cargar_pokedex(nombre_archivo): 
    pokedex = HashMap() 
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as archivo: 
            datos = json.load(archivo) 
    except FileNotFoundError: 
        print("No se encontró el archivo.") 
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

def main():
    pokedex = cargar_pokedex("pokemones.json")
    medallas= cargar_medallas()
    entrenador = Entrenador()
    pc = Linked_list_simple()
    curacion = Queue()
    centro = Centro_Pokemon(curacion)
    stack= Stack()
    transferencia= Tranferencia(stack)
    gimnasio= Gimnasio()

    print(pokedex)
    print(cargar_medallas())
    
    contador = 0

    for bucket in pokedex.buckets:
        for clave, poke in bucket:
            entrenador.agregar_pokemon(poke, pc)
            contador += 1
            if contador == 8:
                break
        if contador == 8:
            break
    print("\nEQUIPO:")
    for pokemon in entrenador.equipo:
        print(pokemon)

    print("\nPC:")
    pc.mostrar()
    print()
    
    

    for pokemon in entrenador.equipo:
        centro.ingresar(pokemon)

    centro.curar()
    
    for poke in entrenador.equipo:
        print()
        transferencia.transferir(poke)
    transferencia.deshacer()

    gimnasio.mostrar_gimnasios()

    opcion = int(input("Elegí un gimnasio: "))

    gimnasio.desafiar(opcion, medallas)

    print("\nMedallas obtenidas:")
    print(medallas)

    submenu_sorts(pc)
    nombre = input("Ingrese el nombre del pokemon: ")

    resultado = entrenador.buscar_pokemon(nombre)

    if resultado:
        print("Pokemon encontrado:")
        print(resultado)
    else:
        print("Ese pokemon no esta en el equipo.")



if __name__ == "__main__":
    main()






