from estructuras import Queue, Stack, HashMap, HashSet
import random

class Pokemon:
    def __init__(self, id, nombre, tipo, poder_combate):
        self.id= id
        self.nombre= nombre
        self.tipo= tipo
        self.poder_combate= poder_combate

    def __repr__(self):
        return f"{self.id}: {self.nombre}, {self.tipo}, {self.poder_combate}"


class Entrenador:
    def __init__(self):
        self.equipo=[]

    def __repr__(self):
        resultado = ""

        for pokemon in self.equipo:
            resultado += f"{pokemon}\n"

        return resultado
    
    def atrapar_pokemon(self, pokedex, pc):
        pokemones= []
        for bucket in pokedex.buckets:
            for _, pokemon in bucket:
                pokemones.append(pokemon)
        
        salvaje = random.choice(pokemones)

        print("un pokemon salvaje aparecio!")
        print(f"nombre: {salvaje.nombre}")
        print(f"tipo: {salvaje.tipo}")
        print(f"poder de combate: {salvaje.poder_combate}")

        opcion = input("lanzar una Pokeball? (s/n): ").lower()

        if opcion == "s":

            intento = random.randint(1, 100)

            if intento <= 70:
                print("atrapaste al pokemon")
                self.agregar_pokemon(salvaje, pc)
            else:
                print("la Pokeball fallo, el Pokemon escapo")
        
        else:
            print("escapaste del combate")
            return

    def agregar_pokemon(self, pokemon, pc):
        if len(self.equipo)< 6:
            self.equipo.append(pokemon)
            print(f"{pokemon.nombre}agregado a su equipo")
        else:
            print("equipo lleno, enviando a la pc")
            pc.agregar(pokemon)
    
    def buscar_pokemon(self, nombre):
        for pokemon in self.equipo:
            if pokemon.nombre.lower() == nombre.lower():
                return pokemon
            return None
        
class Centro_Pokemon():

    def __init__(self, cola):
        self.cola= cola
    
    def ingresar(self, pokemon):
        self.cola.enqueue(pokemon)
    
    def curar(self):
        while not self.cola.is_empty():
            pokemon = self.cola.dequeue()
            print(f"Curando a tu {pokemon.nombre}")

class Tranferencia:
    def __init__(self, stack):
        self.stack = stack
    
    def transferir(self, pokemon):
        self.stack.push(pokemon)

        if self.stack.size() > 5:
            self.stack.items.pop(0)

        print(f"{pokemon.nombre} se transfirio correctamente")
    
    def deshacer(self):
        pokemon= self.stack.pop()

        if pokemon:
            print(f"{pokemon.nombre} regreso correctamente")
            return pokemon
        
        print("no hay transferencias para cancelar")
        return None
    
class Gimnasio:
    def __init__(self):
        self.gimnasios = [
            "Roca",
            "Cascada",
            "Trueno",
            "Arcoiris",
            "Alma",
            "Pantano",
            "Volcan",
            "Tierra"
        ]

    def mostrar_gimnasios(self):
        print("gimnasios: ")
        for i, gimnasio in enumerate(self.gimnasios, start=1):
            print(f"{i}. {gimnasio}")

    def desafiar(self, opcion, medallas):
        if opcion < 1 or opcion > len(self.gimnasios):
            print("gimnasio invaido.")
            return

        gimnasio = self.gimnasios[opcion - 1]

        print(f"\nDesafiando al gimnasio {gimnasio}")

        if random.choice([True, False]):
            print("Ganaste el combate!")
            medallas.add(f"Medalla {gimnasio}")
        else:
            print("Perdiste el combate")

    


        




