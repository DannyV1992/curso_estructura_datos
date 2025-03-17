from nueva_cola import nueva_cola

mi_cola = nueva_cola(5)

print("esta vacia? " + str(mi_cola.is_empty()))
mi_cola.enqueue("3030")
print("esta vacia? " + str(mi_cola.is_empty()))
mi_cola.enqueue(20)
print("saco de la cola " + str(mi_cola.dequeue()))
print("saco de la cola " + str(mi_cola.dequeue()))
print("esta vacia? " + str(mi_cola.is_empty()))