import time  # Proporciona varias funciones para trabajar con tiempo
import os  # Importa el módulo os para manejo de rutas de archivos

# ------------------------------Archivos de salida por año-------------------------------
def save_results_to_csv(punt_plays, algorithm_name, year):  # Función para guardar resultados en CSV
    current_dir = os.path.dirname(os.path.abspath(__file__))  # os.path.abspath(__file__) obtiene la ruta del archivo .py y os.path.dirname del directorio ("C:\\Users\\usuario\\Documents\\tarea_programada_1\\PRIMERA_PARTE").
    output_dir = os.path.join(current_dir, "archivos_ordenados")  # Construye ruta para carpeta de salida agregando \\archivos_ordenados a la direccion
    
    output_filename = f"PARTE1_{algorithm_name}_resultado_{year}.csv"  # Genera nombre del archivo de salida
    output_path = os.path.join(output_dir, output_filename)  # Construye ruta completa del archivo
    
    try:
        with open(output_path, 'w', encoding='utf-8', newline='') as file:  # Abre archivo en modo escritura
            headers = "GameID,Teams,Yards_Gained,Quarter,Date,Time\n"  # Define encabezados del CSV
            file.write(headers)  # Escribe encabezados
            
            for play in punt_plays:  # Itera sobre cada jugada
                file.write(f"{str(play)}\n")  # Escribe cada jugada en el archivo. Aqui se usa explicitamente el __str__ modificado en PuntPlay
        print(f"Archivo guardado exitosamente en: {output_path}")  # Confirma guardado exitoso
    except Exception as e:
        print(f"Error al guardar el archivo {output_filename}: {str(e)}")  # Maneja errores de escritura

# ------------------------------Bubble Sort--------------------------------
def bubble_sort(punt_plays, year):  # Implementación de Bubble Sort
    comparaciones = 0  # Contador de comparaciones
    intercambios = 0  # Contador de intercambios
    tiempo_inicio = time.time()  # Registra tiempo inicial
    
    n = len(punt_plays)  # Obtiene longitud de la lista
    for i in range(0, n):  # Itera sobre la lista
        for j in range(0, n-1-i):  # Itera sobre elementos no ordenados
            comparaciones += 1  # Incrementa contador de comparaciones
            if punt_plays[j+1] < punt_plays[j]:  # Compara elementos adyacentes. Usa el operador sobreescrito en punt_plays. punt_plays[j] es la jugada actual y punt_plays[j+1] es la siguiente jugada
                intercambios += 1  # Incrementa contador de intercambios
                punt_plays[j], punt_plays[j+1] = punt_plays[j+1], punt_plays[j]  # Intercambia elementos. La coma es usada para hacer asignaciones multiples, es decir punt_plays[j] = punt_plays[j+1] y punt_plays[j+1] = punt_plays[j]
    
    tiempo_total = time.time() - tiempo_inicio  # Calcula tiempo total
    
    # save_results_to_csv(punt_plays, "BUBBLE") # Se usa para cuando se quiere guardar todos los años en un solo archivo
    save_results_to_csv(punt_plays, "BUBBLE", year)  # Guarda resultados

    return {  # Retorna un diccionario con las estadísticas de ejecución
        "tiempo_inicio": time.strftime("%H:%M:%S", time.localtime(tiempo_inicio)),  # Convierte el timestamp inicial a formato hora:minuto:segundo
        "tiempo_final": time.strftime("%H:%M:%S", time.localtime(time.time())),    # Convierte el timestamp actual a formato hora:minuto:segundo
        "duracion": f"{tiempo_total:.2f} segundos",  # Formatea el tiempo total con 2 decimales y añade "segundos"
        "comparaciones": comparaciones,  # Número total de comparaciones realizadas
        "intercambios": intercambios     # Número total de intercambios realizados
    }

# ------------------------------Insertion Sort--------------------------------
def insertion_sort(punt_plays, year):  # Implementación de Insertion Sort
    comparaciones = 0  # Contador de comparaciones
    intercambios = 0  # Contador de intercambios
    tiempo_inicio = time.time()  # Registra tiempo inicial
    
    for i in range(1, len(punt_plays)):  # Itera desde el segundo elemento ya que este algoritmo supone que el primer elemnto esta en la posicion correcta
        v = punt_plays[i]  # Elemento actual a insertar
        j = i - 1  # Índice del elemento anterior
        while j >= 0:  # Mientras haya elementos para comparar
            comparaciones += 1  # Incrementa contador de comparaciones
            if punt_plays[j] > v:  # Compara elementos
                punt_plays[j + 1] = punt_plays[j]  # Mueve elemento mayor
                intercambios += 1  # Incrementa contador de intercambios
                j = j - 1  # Retrocede en la lista
            else:
                break  # Sale si encuentra posición correcta
        punt_plays[j + 1] = v  # Inserta elemento en posición correcta
    
    tiempo_total = time.time() - tiempo_inicio  # Calcula tiempo total
    save_results_to_csv(punt_plays, "INSERTION", year)  # Guarda resultados

    return {  # Retorna un diccionario con las estadísticas de ejecución
        "tiempo_inicio": time.strftime("%H:%M:%S", time.localtime(tiempo_inicio)),  # Convierte el timestamp inicial a formato hora:minuto:segundo
        "tiempo_final": time.strftime("%H:%M:%S", time.localtime(time.time())),    # Convierte el timestamp actual a formato hora:minuto:segundo
        "duracion": f"{tiempo_total:.2f} segundos",  # Formatea el tiempo total con 2 decimales y añade "segundos"
        "comparaciones": comparaciones,  # Número total de comparaciones realizadas
        "intercambios": intercambios     # Número total de intercambios realizados
    }

"""
Lista inicial: [5, 2, 4, 1, 3]
Iteración con v = 2
j comienza en 0 (posición del 5)
Como 5 > 2:
  - Mueve el 5 una posición adelante
  - j = j - 1 (j ahora es -1)
  - Sale del while porque j < 0
punt_plays[j + 1] = v coloca el 2 en la posición 0
Resultado: [2, 5, 4, 1, 3]
"""

# ------------------------------Merge Sort Recursivo--------------------------------
def merge(left, right, comparaciones, intercambios):  # Función auxiliar para combinar dos sublistas ordenadas
    result = []  # Lista resultado donde se combinarán las sublistas
    i, j = 0, 0  # Índices para recorrer las sublistas left y right
    
    while i < len(left) and j < len(right):  # Mientras haya elementos por comparar en ambas sublistas
        comparaciones += 1  # Incrementa contador de comparaciones
        if left[i] <= right[j]:  # Compara elementos de ambas sublistas
            result.append(left[i])  # Agrega elemento de left si es menor o igual
            i += 1  # Avanza en la sublista left
        else:
            result.append(right[j])  # Agrega elemento de right si es menor
            j += 1  # Avanza en la sublista right
            intercambios += 1  # Incrementa contador de intercambios
            
    result.extend(left[i:])  # Agrega elementos restantes de left
    result.extend(right[j:])  # Agrega elementos restantes de right
    return result, comparaciones, intercambios  # Retorna lista ordenada y contadores

def mergesort_recursive(punt_plays, year):  # Implementación principal de Merge Sort recursivo
    tiempo_inicio = time.time()  # Registra tiempo inicial
    comparaciones = 0  # Inicializa contador de comparaciones
    intercambios = 0  # Inicializa contador de intercambios
    
    def _mergesort(l):  # Función recursiva interna del algoritmo
        nonlocal comparaciones, intercambios  # Permite modificar contadores externos
        if len(l) < 2:  # Caso base: lista de 0 o 1 elemento
            return l[:]  # Retorna copia de la lista
        else:
            middle = len(l) // 2  # Calcula punto medio
            left = _mergesort(l[:middle])  # Ordena mitad izquierda recursivamente
            right = _mergesort(l[middle:])  # Ordena mitad derecha recursivamente
            merged, comp, inter = merge(left, right, comparaciones, intercambios)  # Combina sublistas ordenadas
            comparaciones = comp  # Actualiza contador de comparaciones
            intercambios = inter  # Actualiza contador de intercambios
            return merged  # Retorna lista combinada y ordenada
    
    punt_plays[:] = _mergesort(punt_plays)  # Aplica el ordenamiento a la lista original
    tiempo_total = time.time() - tiempo_inicio  # Calcula tiempo total

    save_results_to_csv(punt_plays, "MERGE_RECURSIVO", year)  # Guarda resultados en archivo CSV
    
    return {  # Retorna diccionario con estadísticas
        "tiempo_inicio": time.strftime("%H:%M:%S", time.localtime(tiempo_inicio)),
        "tiempo_final": time.strftime("%H:%M:%S", time.localtime(time.time())),
        "duracion": f"{tiempo_total:.2f} segundos",
        "comparaciones": comparaciones,
        "intercambios": intercambios
    }

# ------------------------------Merge Sort Iterativo--------------------------------
def mergesort_iterative(punt_plays, year):
    tiempo_inicio = time.time()  # Registra el tiempo de inicio
    comparaciones = 0  # Inicializa contador de comparaciones
    intercambios = 0  # Inicializa contador de intercambios
    n = len(punt_plays)  # Obtiene longitud de la lista
    width = 1  # Inicializa el tamaño de los subarreglos a combinar
    
    def merge_nr(a, l, m, r):  # Función interna para combinar subarreglos
        nonlocal comparaciones, intercambios  # Permite modificar contadores externos
        n1 = m - l + 1  # Calcula tamaño del subarreglo izquierdo
        n2 = r - m  # Calcula tamaño del subarreglo derecho
        L = [a[l + i] for i in range(n1)]  # Crea copia del subarreglo izquierdo
        R = [a[m + 1 + i] for i in range(n2)]  # Crea copia del subarreglo derecho
        
        i, j, k = 0, 0, l  # Inicializa índices para combinar
        while i < n1 and j < n2:  # Mientras haya elementos en ambos subarreglos
            comparaciones += 1  # Incrementa contador de comparaciones
            if L[i] <= R[j]:  # Compara elementos de ambos subarreglos
                a[k] = L[i]  # Coloca elemento de L en posición correcta
                i += 1  # Avanza en subarreglo izquierdo
            else:
                a[k] = R[j]  # Coloca elemento de R en posición correcta
                j += 1  # Avanza en subarreglo derecho
                intercambios += 1  # Incrementa contador de intercambios
            k += 1  # Avanza en arreglo principal
            
        while i < n1:  # Copia elementos restantes de L
            a[k] = L[i]  # Coloca elemento en posición final
            i += 1  # Avanza en subarreglo izquierdo
            k += 1  # Avanza en arreglo principal
        while j < n2:  # Copia elementos restantes de R
            a[k] = R[j]  # Coloca elemento en posición final
            j += 1  # Avanza en subarreglo derecho
            k += 1  # Avanza en arreglo principal
    
    while width < n:  # Mientras el tamaño de subarreglo sea menor que la lista
        l = 0  # Inicializa índice izquierdo
        while l < n:  # Procesa toda la lista
            r = min(l + (width * 2 - 1), n - 1)  # Calcula índice derecho
            m = min(l + width - 1, n - 1)  # Calcula punto medio
            merge_nr(punt_plays, l, m, r)  # Combina subarreglos
            l += width * 2  # Avanza al siguiente par de subarreglos
        width *= 2  # Duplica tamaño de subarreglos
    
    tiempo_total = time.time() - tiempo_inicio  # Calcula tiempo total

    save_results_to_csv(punt_plays, "MERGE_ITERATIVO", year)  # Guarda resultados en CSV

    return {  # Retorna estadísticas de ejecución
        "tiempo_inicio": time.strftime("%H:%M:%S", time.localtime(tiempo_inicio)),
        "tiempo_final": time.strftime("%H:%M:%S", time.localtime(time.time())),
        "duracion": f"{tiempo_total:.2f} segundos",
        "comparaciones": comparaciones,
        "intercambios": intercambios
    }

# ------------------------------Quick Sort Recursivo--------------------------------
def quicksort_recursive(punt_plays, year):  # Función principal de Quick Sort recursivo
    tiempo_inicio = time.time()  # Registra el tiempo de inicio
    comparaciones = 0  # Inicializa contador de comparaciones
    intercambios = 0  # Inicializa contador de intercambios
    
    def partition(arr, low, high):  # Función para particionar el array
        nonlocal comparaciones, intercambios  # Permite modificar contadores del scope exterior
        pivot = arr[high]  # Selecciona el último elemento como pivote
        i = low - 1  # Índice del elemento más pequeño
        
        for j in range(low, high):  # Recorre subarreglo
            comparaciones += 1  # Incrementa contador de comparaciones
            if arr[j] < pivot:  # Compara elemento actual con pivote
                i += 1  # Incrementa índice del elemento más pequeño
                arr[i], arr[j] = arr[j], arr[i]  # Intercambia elementos
                intercambios += 1  # Incrementa contador de intercambios
        
        arr[i + 1], arr[high] = arr[high], arr[i + 1]  # Coloca pivote en su posición final
        intercambios += 1  # Incrementa contador por el intercambio del pivote
        return i + 1  # Retorna la posición final del pivote
    
    def _quicksort(arr, low, high):  # Función recursiva de Quick Sort
        if low < high:  # Condición base: más de un elemento
            pi = partition(arr, low, high)  # Obtiene índice de partición
            _quicksort(arr, low, pi - 1)  # Ordena subarray izquierdo
            _quicksort(arr, pi + 1, high)  # Ordena subarray derecho
    
    _quicksort(punt_plays, 0, len(punt_plays) - 1)  # Inicia ordenamiento del array completo
    
    tiempo_total = time.time() - tiempo_inicio  # Calcula tiempo total de ejecución

    save_results_to_csv(punt_plays, "QUICK_RECURSIVO", year)  # Guarda resultados en CSV

    return {  # Retorna diccionario con estadísticas
        "tiempo_inicio": time.strftime("%H:%M:%S", time.localtime(tiempo_inicio)),
        "tiempo_final": time.strftime("%H:%M:%S", time.localtime(time.time())),
        "duracion": f"{tiempo_total:.2f} segundos",
        "comparaciones": comparaciones,
        "intercambios": intercambios
    }

# ------------------------------Quick Sort Iterativo--------------------------------
def quicksort_iterative(punt_plays, year):  # Función principal de QuickSort iterativo
    tiempo_inicio = time.time()  # Registra tiempo inicial de ejecución
    comparaciones = 0  # Inicializa contador de comparaciones
    intercambios = 0  # Inicializa contador de intercambios
    
    def partition(arr, l, h):  # Función auxiliar para particionar el array
        nonlocal comparaciones, intercambios  # Permite modificar contadores dentro de la función
        x = arr[h]  # Selecciona el pivote (último elemento)
        i = l - 1  # Inicializa índice para elementos menores que el pivote
        
        for j in range(l, h):  # Recorre subarreglo
            comparaciones += 1  # Incrementa contador de comparaciones
            if arr[j] <= x:  # Compara elemento actual con pivote
                i += 1  # Avanza índice de elementos menores
                arr[i], arr[j] = arr[j], arr[i]  # Intercambia elementos
                intercambios += 1  # Incrementa contador de intercambios
        
        arr[i + 1], arr[h] = arr[h], arr[i + 1]  # Coloca pivote en su posición final
        intercambios += 1  # Incrementa contador por el intercambio del pivote
        return i + 1  # Retorna posición final del pivote
    
    l = 0  # Índice inicial del array
    h = len(punt_plays) - 1  # Índice final del array
    size = h - l + 1  # Calcula tamaño del array
    stack = [0] * size  # Crea pila para almacenar índices
    top = -1  # Inicializa tope de la pila
    
    top += 1  # Incrementa tope
    stack[top] = l  # Apila índice inicial
    top += 1  # Incrementa tope
    stack[top] = h  # Apila índice final
    
    while top >= 0:  # Mientras haya elementos en la pila
        h = stack[top]  # Obtiene índice final del subarreglo actual
        top -= 1  # Decrementa tope
        l = stack[top]  # Obtiene índice inicial del subarreglo actual
        top -= 1  # Decrementa tope
        
        p = partition(punt_plays, l, h)  # Particiona el subarreglo actual
        
        if p - 1 > l:  # Si hay elementos a la izquierda del pivote
            top += 1  # Incrementa tope
            stack[top] = l  # Apila índice inicial del subarreglo izquierdo
            top += 1  # Incrementa tope
            stack[top] = p - 1  # Apila índice final del subarreglo izquierdo
            
        if p + 1 < h:  # Si hay elementos a la derecha del pivote
            top += 1  # Incrementa tope
            stack[top] = p + 1  # Apila índice inicial del subarreglo derecho
            top += 1  # Incrementa tope
            stack[top] = h  # Apila índice final del subarreglo derecho
    
    tiempo_total = time.time() - tiempo_inicio  # Calcula tiempo total de ejecución

    save_results_to_csv(punt_plays, "QUICK_ITERATIVO", year)  # Guarda resultados en archivo CSV

    return {  # Retorna estadísticas de ejecución
        "tiempo_inicio": time.strftime("%H:%M:%S", time.localtime(tiempo_inicio)),
        "tiempo_final": time.strftime("%H:%M:%S", time.localtime(time.time())),
        "duracion": f"{tiempo_total:.2f} segundos",
        "comparaciones": comparaciones,
        "intercambios": intercambios
    }