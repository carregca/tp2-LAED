import json
from estructuras import HashSet, HashMap, Nodo, linked_list_simple, centro_pokemon
from clases import Pokemon, Entrenador

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
    entrenador = Entrenador()
    pc = linked_list_simple()

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


if __name__ == "__main__":
    main()






