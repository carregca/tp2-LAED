from estructuras import Queue, Stack
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

    def agregar_pokemon(self, pokemon, pc):
        if len(self.equipo)< 6:
            self.equipo.append(pokemon)
            print(f"{pokemon.nombre}agregado a su equipo")
        else:
            print("equipo lleno, enviando a la pc")
            pc.agregar(pokemon)

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

    


        




