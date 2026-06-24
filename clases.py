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


