import json
class pokemon:
    def __init__(self, id, nombre, tipo, poder_combate):
        self.id= id
        self.nombre= nombre
        self.tipo= tipo
        self.poder_combate= poder_combate

    def __repr__(self):
        return f"{self.id}: {self.nombre}, {self.tipo}, {self.poder_combate}"

#clase de hashmap sacada de w3schools
class simple_hashmap:
    def __init__(self, size=100):
        self.size = size
        self.buckets = [[] for _ in range(size)] 
    
    def __repr__(self):
        resultado = ""
        for bucket in self.buckets:
            for id, pokemon in bucket:
                    resultado += f"{pokemon}\n"
        return resultado
        
    def hash_function(self, key):
        key = str(key)
        numeric_sum = sum(int(char) for char in key if char.isdigit())
        return numeric_sum % self.size 

    def put(self, key, value):
        index = self.hash_function(key)
        bucket = self.buckets[index]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))
    
    def print_map(self):
        print("Hash Map Contents:")
        for index, bucket in enumerate(self.buckets):
            print(f"Bucket {index}: {bucket}")
            
    def mostrar_todos(self):
        for bucket in self.buckets:
            for clave, pokemon in bucket:
                print(pokemon)
        
        pokedex = simple_hashmap()
        
        with open("pokemones.json", "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)
        for p in datos:
            poke = pokemon(p["id"], p["nombre"], p["tipo"], p["poder_combate"])
            pokedex.put(poke.id, poke)
        return pokedex


class Registro_Medallas:
    def __init__(self, size=10):
        self.size=size
        self.buckets = [[] for i in range(size)]

    def hash_function(self, value):
        return sum(ord(char) for char in value) % self.size
    
    def add(self, value):
        index = self.hash_function(value)
        bucket = self.buckets[index]
        if value not in bucket:
            bucket.append(value)
    
    def __repr__(self):
        resultado = ""

        for bucket in self.buckets:
            for medalla in bucket:
                resultado += f"{medalla}\n"

        return resultado

def cargar_medallas():
    medallas = Registro_Medallas()
    with open("medallas_jugador.json", "r", encoding="utf-8") as archivo:
        datos = json.load(archivo)
    for m in datos:
        medallas.add(m)
    return medallas

simple_hashmap.mostrar_todos()

print(cargar_medallas())


