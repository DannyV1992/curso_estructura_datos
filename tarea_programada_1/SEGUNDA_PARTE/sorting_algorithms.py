import time
import os
from play_comparator import PlayComparator
import sys # Importa el módulo sys que proporciona acceso a algunas variables y funciones utilizadas o mantenidas por el intérprete de Python
sys.setrecursionlimit(3000) # Aumenta el límite de recursión del sistema a 3000 llamadas (por default es 1000)

# ------------------------------Archivos de salida por año-------------------------------
def save_results_to_csv(punt_plays, algorithm_name, year):  # Función para guardar resultados en CSV
    current_dir = os.path.dirname(os.path.abspath(__file__))  # os.path.abspath(__file__) obtiene la ruta del archivo .py y os.path.dirname del directorio ("C:\\Users\\usuario\\Documents\\tarea_programada_1\\PRIMERA_PARTE").
    output_dir = os.path.join(current_dir, "archivos_ordenados")  # Construye ruta para carpeta de salida agregando \\archivos_ordenados a la direccion
    
    output_filename = f"PARTE2_{algorithm_name}_resultado_{year}.csv"  # Genera nombre del archivo de salida
    output_path = os.path.join(output_dir, output_filename)  # Construye ruta completa del archivo
    
    try:
        with open(output_path, 'w', encoding='utf-8', newline='') as file:  # Abre archivo en modo escritura
            headers = "GameID,Teams,Yards_Gained,Quarter,Date,Time\n"  # Define encabezados del CSV
            file.write(headers)  # Escribe encabezados
            
            for play in punt_plays:  # Itera sobre cada jugada
                file.write(f"{str(play)}\n")  # Escribe cada jugada en el archivo. Aqui se usa explicitamente el __str__ modificado en PuntPlay
        print(f"Archivo guardado exitosamente en: {output_path}")  # Confirma guardado exitoso
    except Exception as e:
        print(f"Error al guardar el archivo {output_filename}: {str(e)}")  # Maneja errores de escritura. e funciona como una variable para almacenar el tipo de error
        
# ------------------------------Bubble Sort--------------------------------
def bubble_sort(punt_plays, year):  # Implementación de Bubble Sort
    comparator = PlayComparator()  # Instancia de PlayComparator para comparar jugadas
    tiempo_inicio = time.time()  # Registra el tiempo inicial
    
    for i in range(0, len(punt_plays)):  # Itera sobre toda la lista de jugadas
        for j in range(0, len(punt_plays)-1-i):  # Itera sobre los elementos no ordenados
            if comparator.compare(punt_plays[j], punt_plays[j+1]) > 0:  # Compara dos jugadas adyacentes usando PlayComparator
                punt_plays[j], punt_plays[j+1] = punt_plays[j+1], punt_plays[j]  # Intercambia las jugadas si están desordenadas
    
    tiempo_total = time.time() - tiempo_inicio  # Calcula el tiempo total de ejecución
    save_results_to_csv(punt_plays, "BUBBLE", year)  # Guarda los resultados ordenados en un archivo CSV
    
    return {  # Retorna un diccionario con las estadísticas de ejecución
        "tiempo_inicio": time.strftime("%H:%M:%S", time.localtime(tiempo_inicio)),  # Convierte el timestamp inicial a formato hora:minuto:segundo
        "tiempo_final": time.strftime("%H:%M:%S", time.localtime(time.time())),    # Convierte el timestamp final a formato hora:minuto:segundo
        "duracion": f"{tiempo_total:.2f} segundos"  # Tiempo total formateado con dos decimales y unidad "segundos"
    }

# ------------------------------Insertion Sort--------------------------------
def insertion_sort(punt_plays, year):  # Implementación de Insertion Sort
    comparator = PlayComparator()  # Instancia de PlayComparator para comparar jugadas
    tiempo_inicio = time.time()  # Registra el tiempo inicial
    
    for i in range(1, len(punt_plays)):  # Itera desde el segundo elemento hasta el final de la lista
        key = punt_plays[i]  # Almacena la jugada actual como clave temporal
        j = i - 1  # Inicializa un índice para comparar con elementos anteriores
        
        while j >= 0 and comparator.compare(punt_plays[j], key) > 0:  # Compara las jugadas usando PlayComparator mientras estén desordenadas
            punt_plays[j + 1] = punt_plays[j]  # Desplaza la jugada hacia adelante si está desordenada
            j -= 1  # Decrementa el índice para seguir comparando con elementos anteriores
        
        punt_plays[j + 1] = key  # Inserta la clave en su posición correcta
    
    tiempo_total = time.time() - tiempo_inicio  # Calcula el tiempo total de ejecución
    save_results_to_csv(punt_plays, "INSERTION", year)  # Guarda los resultados ordenados en un archivo CSV
    
    return {  
        "tiempo_inicio": time.strftime("%H:%M:%S", time.localtime(tiempo_inicio)),  
        "tiempo_final": time.strftime("%H:%M:%S", time.localtime(time.time())),    
        "duracion": f"{tiempo_total:.2f} segundos"  
    }

# ------------------------------Merge Sort Recursivo--------------------------------
def merge(left, right, comparator):
    result = []
    i, j = 0, 0
    
    while i < len(left) and j < len(right):
        if comparator.compare(left[i], right[j]) <= 0:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def mergesort_recursive(punt_plays, year):
    comparator = PlayComparator()
    tiempo_inicio = time.time()
    
    def _mergesort(arr):
        if len(arr) < 2:
            return arr[:]
        else:
            middle = len(arr) // 2
            left = _mergesort(arr[:middle])
            right = _mergesort(arr[middle:])
            return merge(left, right, comparator)
    
    punt_plays[:] = _mergesort(punt_plays)
    
    tiempo_total = time.time() - tiempo_inicio
    save_results_to_csv(punt_plays, "MERGE_RECURSIVO", year)
    
    return {
        "tiempo_inicio": time.strftime("%H:%M:%S", time.localtime(tiempo_inicio)),
        "tiempo_final": time.strftime("%H:%M:%S", time.localtime(time.time())),
        "duracion": f"{tiempo_total:.2f} segundos"
    }

# ------------------------------Merge No Sort Recursivo--------------------------------
def mergesort_iterative(punt_plays, year):  # Implementación de Merge Sort iterativo
    tiempo_inicio = time.time()  # Registra el tiempo inicial
    comparator = PlayComparator()  # Instancia del comparador para comparar jugadas
    n = len(punt_plays)  # Longitud de la lista
    width = 1  # Tamaño inicial de los subarreglos a combinar
    
    while width < n:  # Incrementa el tamaño del subarreglo en cada iteración
        l = 0  # Índice inicial del subarreglo
        while l < n:  # Procesa todos los subarreglos en la lista
            r = min(l + (width * 2 - 1), n - 1)  # Índice final del subarreglo derecho
            m = min(l + width - 1, n - 1)  # Índice final del subarreglo izquierdo
            
            # Divide la lista en dos subarreglos y los combina
            left = punt_plays[l:m+1]  # Subarreglo izquierdo
            right = punt_plays[m+1:r+1]  # Subarreglo derecho
            
            merged = merge(left, right, comparator)  # Combina los subarreglos usando el comparador
            punt_plays[l:r+1] = merged  # Reemplaza los elementos originales con los combinados
            l += width * 2  # Avanza al siguiente par de subarreglos
        
        width *= 2  # Duplica el tamaño del subarreglo para la siguiente iteración
    
    tiempo_total = time.time() - tiempo_inicio  # Calcula el tiempo total de ejecución
    save_results_to_csv(punt_plays, "MERGE_ITERATIVO", year)  # Guarda los resultados ordenados en un archivo CSV
    
    return {  
        "tiempo_inicio": time.strftime("%H:%M:%S", time.localtime(tiempo_inicio)),  
        "tiempo_final": time.strftime("%H:%M:%S", time.localtime(time.time())),    
        "duracion": f"{tiempo_total:.2f} segundos"  
    }

# ------------------------------Quick Sort Recursivo--------------------------------
def quicksort_recursive(punt_plays, year):  # Implementación de Quick Sort recursivo
    tiempo_inicio = time.time()  # Registra el tiempo inicial
    comparator = PlayComparator()  # Instancia del comparador para comparar jugadas
    
    def partition(arr, low, high):  
        pivot = arr[high]  # Selecciona el último elemento como pivote
        i = low - 1  # Índice del menor elemento
        
        for j in range(low, high):  
            if comparator.compare(arr[j], pivot) <= 0:  # Compara el elemento actual con el pivote
                i += 1  
                arr[i], arr[j] = arr[j], arr[i]  # Intercambia elementos si están desordenados
        
        arr[i + 1], arr[high] = arr[high], arr[i + 1]  # Coloca el pivote en su posición correcta
        return i + 1  
    
    def _quicksort(arr, low, high):  
        if low < high:  
            pi = partition(arr, low, high)  # Encuentra la posición del pivote
            _quicksort(arr, low, pi - 1)  # Ordena la parte izquierda del pivote
            _quicksort(arr, pi + 1, high)  # Ordena la parte derecha del pivote
    
    _quicksort(punt_plays, 0, len(punt_plays) - 1)  
    
    tiempo_total = time.time() - tiempo_inicio  
    save_results_to_csv(punt_plays, "QUICK_RECURSIVO", year)  
    
    return {  
        "tiempo_inicio": time.strftime("%H:%M:%S", time.localtime(tiempo_inicio)),  
        "tiempo_final": time.strftime("%H:%M:%S", time.localtime(time.time())),    
        "duracion": f"{tiempo_total:.2f} segundos"  
    }

# ------------------------------Quick No Sort Recursivo--------------------------------
def quicksort_iterative(punt_plays, year):  # Implementación de Quick Sort iterativo
    tiempo_inicio = time.time()  # Registra el tiempo inicial
    comparator = PlayComparator()  # Instancia del comparador para comparar jugadas
    
    def partition(arr, l, h):  
        pivot = arr[h]  # Selecciona el último elemento como pivote
        i = l - 1  
        
        for j in range(l, h):  
            if comparator.compare(arr[j], pivot) <= 0:  
                i += 1  
                arr[i], arr[j] = arr[j], arr[i]   # Intercambia elementos si están desordenados
        
        arr[i + 1], arr[h] = arr[h], arr[i + 1]   # Coloca el pivote en su posición correcta
        return i + 1  
    
    stack = []   # Pila para almacenar índices de las particiones pendientes
    stack.append(0)   # Índice inicial de la lista
    stack.append(len(punt_plays) - 1)   # Índice final de la lista
    
    while stack:   # Mientras haya particiones pendientes en la pila
        h = stack.pop()   # Obtiene el índice superior (derecho)
        l = stack.pop()   # Obtiene el índice inferior (izquierdo)
        
        p = partition(punt_plays, l, h)   # Encuentra la posición del pivote
        
        if p - 1 > l:   # Si hay elementos a la izquierda del pivote
            stack.append(l)   # Agrega los índices a la pila para procesarlos después
            stack.append(p - 1)
        
        if p + 1 < h:   # Si hay elementos a la derecha del pivote
            stack.append(p + 1)
            stack.append(h)
    
    tiempo_total = time.time() - tiempo_inicio   # Calcula el tiempo total de ejecución
    
    save_results_to_csv(punt_plays, "QUICK_ITERATIVO", year)   # Guarda los resultados ordenados en un archivo CSV
    
    return {  
        "tiempo_inicio": time.strftime("%H:%M:%S", time.localtime(tiempo_inicio)),  
        "tiempo_final": time.strftime("%H:%M:%S", time.localtime(time.time())),    
        "duracion": f"{tiempo_total:.2f} segundos"  
    }