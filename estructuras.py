class Nodo:
    def __init__(self, pokemon):
        self.pokemon = pokemon
        self.next = None

class linked_list_simple:
    def __init__(self):
        self.head = None
    def agregar(self, pokemon):
        nuevo = Nodo(pokemon)
        if self.head is None:
            self.head = nuevo
            return
        actual = self.head
        while actual.next:
            actual = actual.next
        actual.next = nuevo
    def mostrar(self):
        actual = self.head
        while actual:
            print(actual.pokemon)
            actual = actual.next


class HashSet:
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


class HashMap:
    def __init__(self, size=100):
        self.size = size
        self.buckets = [[] for _ in range(size)] 
        
    def hash_function(self, key):
        return int(key)

    def put(self, key, value):
        index = self.hash_function(key)
        bucket = self.buckets[index]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))
    
    def __repr__(self):
        resultado = ""
        for bucket in self.buckets:
            for id, pokemon in bucket:
                    resultado += f"{pokemon}\n"
        return resultado

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, elemento):
        self.items.append(elemento)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

