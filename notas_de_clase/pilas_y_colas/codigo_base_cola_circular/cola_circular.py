class cola_circular:
    def __init__(self, capacidad):
        #Inicializa la cola circular con una capacidad fija.
        self.capacidad = capacidad
        self.cola = [None] * capacidad  # Lista fija
        self.frente = 0  # Índice del elemento frontal
        self.final = 0  # Índice de inserción del próximo elemento
        self.tamano = 0  # Cantidad de elementos en la cola

    def enqueue(self, valor):
        #Agrega un elemento a la cola si hay espacio.
        if self.tamano == self.capacidad:
            raise Exception("La cola está llena")
        
        self.cola[self.final] = valor
        # Avanza circularmente
        self.final = (self.final + 1) % self.capacidad 
        self.tamano += 1

    def dequeue(self):
        #Elimina y retorna el elemento frontal de la cola.#
        if self.tamano == 0:
            raise Exception("La cola está vacía")

        valor = self.cola[self.frente]
        # Opcional, para mayor claridad
        self.cola[self.frente] = None  
        # Avanza circularmente
        self.frente = (self.frente + 1) % self.capacidad  
        self.tamano -= 1
        return valor

    def esta_vacia(self):
        #Verifica si la cola está vacía.#
        return self.tamano == 0

    def esta_llena(self):
        #Verifica si la cola está llena.#
        return self.tamano == self.capacidad

    def __str__(self):
        #Muestra la cola circular en el orden correcto.#
        print(self.cola)
        if self.tamano == 0:
            return "ColaCircular([])"
        
        elementos = []
        indice = self.frente
        for _ in range(self.tamano):
            elementos.append(str(self.cola[indice]))
            # Avanza circularmente
            indice = (indice + 1) % self.capacidad  
        return "ColaCircular([" + ", ".join(elementos) + "])"
