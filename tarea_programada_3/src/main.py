from lista_enlazada_ordenada import ListaEnlazadaOrdenada
from lista_doble_enlazada_ordenada import ListaDobleOrdenada
from cola_prioridad import ColaPrioridad
from persona import Persona

def menu_principal():
    print("\n--- Menú Principal ---")
    print("1. Lista Enlazada Ordenada")
    print("2. Lista Doble Ordenada")
    print("3. Cola de Prioridad")
    print("4. Salir")
    return input("Seleccione una opción: ")

def menu_lista_enlazada(lista):
    while True:
        print("\n--- Menú Lista Enlazada Ordenada ---")
        print("1. Agregar persona")
        print("2. Listar personas")
        print("3. Borrar persona")
        print("4. Buscar personas")
        print("5. Volver al menú principal")
        opcion = input("Seleccione una opción: ")
        if opcion == "5":
            break
        procesar_opcion_lista(lista, opcion)

def menu_lista_doble(lista):
    while True:
        print("\n--- Menú Lista Doblemente Enlazada Ordenada ---")
        print("1. Agregar persona")
        print("2. Listar personas")
        print("3. Borrar persona")
        print("4. Buscar personas")
        print("5. Volver al menú principal")
        opcion = input("Seleccione una opción: ")
        if opcion == "5":
            break
        procesar_opcion_lista(lista, opcion)

def menu_cola_prioridad(cola):
    while True:
        print("\n--- Menú Cola de Prioridad ---")
        print("1. Agregar persona")
        print("2. Listar personas")
        print("3. Atender persona (eliminar)")
        print("4. Volver al menú principal")
        opcion = input("Seleccione una opción: ")
        if opcion == "4":
            break
        procesar_opcion_cola(cola, opcion)

def procesar_opcion_lista(lista, opcion):
    if opcion == "1":
        nombre = input("Nombre: ")
        apellido1 = input("Primer apellido: ")
        apellido2 = input("Segundo apellido: ")
        edad = int(input("Edad: "))
        persona = Persona(nombre, apellido1, apellido2, edad)
        lista.insertar(persona)
    elif opcion == "2":
        lista.imprimir()
    elif opcion == "3":
        posicion = int(input("Posición a borrar: "))
        lista.borrar(posicion)
    elif opcion == "4":
        print("1. Buscar por edad")
        print("2. Buscar por nombre")
        print("3. Buscar por apellido")
        sub_opcion = input("Seleccione tipo de búsqueda: ")
        if sub_opcion == "1":
            edad = int(input("Edad a buscar: "))
            resultados = lista.buscar_por_edad(edad)
        elif sub_opcion == "2":
            nombre = input("Nombre a buscar: ")
            resultados = lista.buscar_por_nombre(nombre)
        elif sub_opcion == "3":
            apellido = input("Apellido a buscar: ")
            resultados = lista.buscar_por_apellido(apellido)
        else:
            print("Opción inválida")
            return
        for persona in resultados:
            print(persona)

def procesar_opcion_cola(cola, opcion):
    if opcion == "1":
        nombre = input("Nombre: ")
        apellido1 = input("Primer apellido: ")
        apellido2 = input("Segundo apellido: ")
        edad = int(input("Edad: "))
        persona = Persona(nombre, apellido1, apellido2, edad)
        cola.insertar(persona)
    elif opcion == "2":
        cola.imprimir()
    elif opcion == "3":
        persona_atendida = cola.eliminar()
        if persona_atendida:
            print(f"Persona atendida: {persona_atendida}")

def main():
    lista_enlazada = ListaEnlazadaOrdenada()
    lista_doble = ListaDobleOrdenada()
    cola_prioridad = ColaPrioridad()

    while True:
        opcion = menu_principal()
        if opcion == "1":
            menu_lista_enlazada(lista_enlazada)
        elif opcion == "2":
            menu_lista_doble(lista_doble)
        elif opcion == "3":
            menu_cola_prioridad(cola_prioridad)
        elif opcion == "4":
            print("Gracias por usar el programa. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()
