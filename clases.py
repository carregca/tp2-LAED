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

        print("¡Un pokemon salvaje apareció!")
        print(f"Nombre: {salvaje.nombre}")
        print(f"Tipo: {salvaje.tipo}")
        print(f"Poder de combate: {salvaje.poder_combate}")

        opcion = input("¿Querés lanzar una Pokeball? (s/n): ").lower()

        if opcion == "s":

            intento = random.randint(1, 100)

            if intento <= 70:
                print("Atrapaste al pokemon")
                self.agregar_pokemon(salvaje, pc)
            else:
                print("La Pokeball falló, el Pokemon escapó")
        
        else:
            print("Escapaste del combate")
            return

    def agregar_pokemon(self, pokemon, pc):
        if len(self.equipo)< 6:
            self.equipo.append(pokemon)
            print(f"{pokemon.nombre} fue agregado a su equipo")
        else:
            print("Equipo lleno, enviando a la pc...")
            pc.agregar(pokemon)
    
    def buscar_pokemon(self, nombre):
        for pokemon in self.equipo:
            if pokemon.nombre.lower() == nombre.lower():
                return pokemon
        return None

    def quitar_pokemon(self, nombre):

        for i, pokemon in enumerate(self.equipo):

            if pokemon.nombre.lower() == nombre.lower():
                return self.equipo.pop(i)
        return None
        
    def mostrar_equipo(self):
        if len(self.equipo) == 0:
            print("El equipo está vacío")
            return

        print("=== Equipo Principal ===")
        for pokemon in self.equipo:
            print(pokemon)
        
    def enviar_a_pc(self, nombre, pc):

        if len(self.equipo) <= 1:
            print("Debes tener al menos un Pokemon en el equipo.")
            return

        pokemon = self.quitar_pokemon(nombre)

        if pokemon:
            pc.agregar(pokemon)
            print(f"{pokemon.nombre} fue enviado a la PC.")
        else:
            print("Pokemon no encontrado.")
    
    def sacar_de_pc(self, pc):
        nombre = input("Nombre del Pokemon: ")
        pokemon = pc.buscar(nombre)
        if pokemon is None:
            print("Ese Pokemon no está en la PC.")
            return
        if len(self.equipo) < 6:
            pc.eliminar(nombre)
            self.equipo.append(pokemon)
            print(f"{pokemon.nombre} pasó al equipo.")
        else:
            print("\nEquipo actual:")
            for i, poke in enumerate(self.equipo):
                print(f"{i+1}. {poke.nombre}")
            opcion = int(input("¿Cuál querés reemplazar?: ")) - 1
            if opcion < 0 or opcion >= len(self.equipo):
                print("Opción inválida.")
                return
            pokemon_equipo = self.equipo[opcion]
            pc.eliminar(nombre)
            pc.agregar(pokemon_equipo)
            self.equipo[opcion] = pokemon
            print(f"{pokemon.nombre} reemplazó a {pokemon_equipo.nombre}.")
        
class Centro_Pokemon():

    def __init__(self, cola):
        self.cola= cola
    
    def ingresar(self, pokemon):
        self.cola.enqueue(pokemon)
    
    def curar(self):
        if self.cola.is_empty():
            print("No hay pokemones esperando")
            return
        
        while not self.cola.is_empty():
            pokemon = self.cola.dequeue()
            print(f"Curando a tu {pokemon.nombre}")
        print("Todos los pokemones han sido curados")

class Tranferencia:
    def __init__(self, stack):
        self.stack = stack
    
    def transferir(self, pc, nombre):
        pokemon = pc.eliminar(nombre)
        if pokemon is None:
            print("Pokemon no encontrado en la PC")
            return
        self.stack.push(pokemon)

        if self.stack.size() > 5: 
            self.stack.items.pop(0)  

        print(f"{pokemon.nombre} Se transfirió correctamente")
    
    def deshacer(self, pc):
        pokemon= self.stack.pop()

        if pokemon:
            pc.agregar(pokemon)
            print(f"{pokemon.nombre} regresó correctamente")
            return pokemon
        else:
            print("No hay transferencias para cancelar")

    
class Gimnasio:
    def __init__(self):
        self.gimnasios = [
            "Roca",
            "Cascada",
            "Trueno",
            "Arcoíris",
            "Alma",
            "Pantano",
            "Volcán",
            "Tierra"
        ]

    def mostrar_gimnasios(self):
        print("Gimnasios: ")
        for i, gimnasio in enumerate(self.gimnasios, start=1):
            print(f"{i}. {gimnasio}")

    def desafiar(self, opcion, medallas):
        if opcion < 1 or opcion > len(self.gimnasios):
            print("Gimnasio inválido.")
            return

        gimnasio = self.gimnasios[opcion - 1]

        print(f"\nDesafiando al gimnasio {gimnasio}")

        if random.choice([True, False]):
            print("¡Ganaste el combate!")
            medallas.add(f"Medalla {gimnasio}")
        else:
            print("Perdiste el combate")