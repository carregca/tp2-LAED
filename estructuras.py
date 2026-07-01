#Estructuras sacadas y modificadas de W3schools

class Nodo:
    def __init__(self, pokemon):
        self.pokemon = pokemon
        self.next = None

class Linked_list_simple:
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
    def convertir_lista(self):
        lista = []
        actual = self.head

        while actual:
            lista.append(actual.pokemon)
            actual = actual.next

        return lista
    
    def buscar(self, nombre):  
        actual = self.head 
        while actual:
            if actual.pokemon.nombre.lower() == nombre.lower():  
                return actual.pokemon 
            actual = actual.next  
        return None  

    def eliminar(self, nombre):  
        actual = self.head 
        anterior = None 

        while actual:  
            if actual.pokemon.nombre.lower() == nombre.lower():  

                if anterior is None: 
                    self.head = actual.next  
                else:  
                    anterior.next = actual.next 

                return actual.pokemon  

            anterior = actual  
            actual = actual.next  

        return None 

    
    #Sorts sacados de w3schools y modificados con mis nombres de variable

    def bubble_sort_nombre(self):
        pokemones= self.convertir_lista()   
        n = len(pokemones)
        for i in range(n-1):
            skew = False 
            for j in range(n-i-1):
                if pokemones[j].nombre > pokemones[j+1].nombre:
                    pokemones[j], pokemones[j+1] = pokemones[j+1], pokemones[j]
                    skew = True
            if not skew:
                break
        return pokemones
    
    def selection_sort_tipo(self):
        pokemones= self.convertir_lista()
        n = len(pokemones)
        for i in range(n):
            min_index = i
            for j in range(i+1, n):
                if pokemones[j].tipo < pokemones[min_index].tipo:
                    min_index = j   
            pokemones[i], pokemones[min_index] = pokemones[min_index], pokemones[i]

        return pokemones 
    
    def quick_sort_pc(self, pokemones=None):

        if pokemones is None:
            pokemones = self.convertir_lista()

        if len(pokemones) <= 1:
            return pokemones

        pivote = pokemones[0]

        mayores = []
        menores = []

        for pokemon in pokemones[1:]:

            if pokemon.poder_combate > pivote.poder_combate:
                mayores.append(pokemon)
            else:
                menores.append(pokemon)

        return self.quick_sort_pc(mayores) + [pivote] + self.quick_sort_pc(menores)
    
     

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

    def get(self, key):
        index = self.hash_function(key)
        bucket = self.buckets[index]

        for ke, pokemon in bucket:
            if ke == key:
                return pokemon
        
        return None
        

    
    def __repr__(self):
        resultado = ""
        for bucket in self.buckets:
            for id, pokemon in bucket:
                    resultado += f"{pokemon}\n"
        return resultado

    def busqueda_binaria(self, id_buscado):
        ids= []

        for bucket in self.buckets:
            if bucket:
                ids.append(bucket[0][0])
        
        izquierda = 0
        derecha = len(ids) - 1

        while izquierda <= derecha:

            medio = (izquierda + derecha) // 2

            if ids[medio] == id_buscado:
                return self.get(id_buscado)

            elif ids[medio] < id_buscado:
                izquierda = medio + 1

            else:
                derecha = medio - 1

        return None
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
    
class Stack:
    def __init__(self):
        self.items = []

    def push(self, elemento):
        self.items.append(elemento)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)