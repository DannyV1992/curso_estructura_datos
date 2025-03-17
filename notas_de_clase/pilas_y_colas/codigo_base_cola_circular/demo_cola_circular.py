from cola_circular import cola_circular

cola = cola_circular(5)  # Crear una cola de tamaño fijo 5

cola.enqueue(10)
cola.enqueue(20)
cola.enqueue(30)
print(cola)  # Muestra la cola

print("Sacando de la cola:", cola.dequeue())  # Elimina el primer elemento
print(cola)

cola.enqueue(40)
cola.enqueue(50)
cola.enqueue(60)
print(cola)

# Intentar encolar otro elemento cuando la cola está llena
try:
    cola.enqueue(70)
except Exception as e:
    print("Error:", e)

cola.dequeue()
cola.dequeue()
print(cola)
cola.enqueue(100)
cola.enqueue(200)
print(cola)
