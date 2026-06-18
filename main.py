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

    def hash_function(self, key):
        numeric_sum = sum(int(char) for char in key if char.isdigit())
        return numeric_sum % 10 

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


pokedex.mostrar_todos()

