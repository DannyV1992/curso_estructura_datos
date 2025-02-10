import time
import os
from play_comparator import PlayComparator

# ------------------------------Archivos de salida por año-------------------------------
def save_results_to_csv(punt_plays, algorithm_name, year):
    # Construir la ruta a la carpeta archivos_ordenados
    current_dir = os.path.dirname(os.path.abspath(__file__))  # os.path.abspath(__file__) obtiene la ruta absoluta del archivo actual y os.path.dirname() sube 1 nivel hasta tarea_programada_1
    output_dir = os.path.join(current_dir, "archivos_ordenados") # os.path.join() construye la ruta completa
        
    # Construir la ruta completa del archivo
    # output_filename = f"PARTE1-{algorithm_name}-resultado.csv" # Para cuando se quiere agrupar todos los años en un mismo archivo
    output_filename = f"PARTE2_{algorithm_name}_resultado_{year}.csv"
    output_path = os.path.join(output_dir, output_filename)
    
    try:
        with open(output_path, 'w', encoding='utf-8', newline='') as file:

            # Escribir encabezados
            headers = "GameID,Teams,Yards_Gained,Quarter,Date,Time\n"
            file.write(headers)

            # Escribir datos
            for play in punt_plays:
                file.write(f"{str(play)}\n")
        print(f"Archivo guardado exitosamente en: {output_path}")
    except Exception as e:
        print(f"Error al guardar el archivo {output_filename}: {str(e)}")

# ------------------------------Bubble Sort--------------------------------
def bubble_sort(punt_plays, year):
    comparator = PlayComparator()
    tiempo_inicio = time.time()
    
    for i in range(0, len(punt_plays)):
        for j in range(0, len(punt_plays)-1-i):
            if comparator.compare(punt_plays[j], punt_plays[j+1]) > 0:
                punt_plays[j], punt_plays[j+1] = punt_plays[j+1], punt_plays[j]
    
    tiempo_total = time.time() - tiempo_inicio
    save_results_to_csv(punt_plays, "BUBBLE", year)
    
    return {
        "tiempo_inicio": time.strftime("%H:%M:%S", time.localtime(tiempo_inicio)),
        "tiempo_final": time.strftime("%H:%M:%S", time.localtime(time.time())),
        "duracion": f"{tiempo_total:.2f} segundos"
    }

# ------------------------------Insertion Sort--------------------------------
def insertion_sort(punt_plays, year):
    comparator = PlayComparator()
    tiempo_inicio = time.time()
    
    for i in range(1, len(punt_plays)):
        key = punt_plays[i]
        j = i - 1
        while j >= 0 and comparator.compare(punt_plays[j], key) > 0:
            punt_plays[j + 1] = punt_plays[j]
            j -= 1
        punt_plays[j + 1] = key
    
    tiempo_total = time.time() - tiempo_inicio
    save_results_to_csv(punt_plays, "INSERTION", year)
    
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
def mergesort_iterative(punt_plays, year):
    comparator = PlayComparator()
    tiempo_inicio = time.time()
    
    width = 1
    n = len(punt_plays)
    
    while width < n:
        l = 0
        while l < n:
            r = min(l + (width * 2 - 1), n - 1)
            m = min(l + width - 1, n - 1)
            
            # Merge subarray usando comparator
            left = punt_plays[l:m+1]
            right = punt_plays[m+1:r+1]
            merged = merge(left, right, comparator)
            
            # Colocar resultado en el array original
            punt_plays[l:r+1] = merged
            l += width * 2
        width *= 2
    
    tiempo_total = time.time() - tiempo_inicio
    save_results_to_csv(punt_plays, "MERGE_ITERATIVO", year)
    
    return {
        "tiempo_inicio": time.strftime("%H:%M:%S", time.localtime(tiempo_inicio)),
        "tiempo_final": time.strftime("%H:%M:%S", time.localtime(time.time())),
        "duracion": f"{tiempo_total:.2f} segundos"
    }

# ------------------------------Quick Sort Recursivo--------------------------------
def quicksort_recursive(punt_plays, year):
    comparator = PlayComparator()
    tiempo_inicio = time.time()
    
    def partition(arr, low, high):
        pivot = arr[high]
        i = low - 1
        
        for j in range(low, high):
            if comparator.compare(arr[j], pivot) <= 0:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1
    
    def _quicksort(arr, low, high):
        if low < high:
            pi = partition(arr, low, high)
            _quicksort(arr, low, pi - 1)
            _quicksort(arr, pi + 1, high)
    
    _quicksort(punt_plays, 0, len(punt_plays) - 1)
    
    tiempo_total = time.time() - tiempo_inicio
    save_results_to_csv(punt_plays, "QUICK_RECURSIVO", year)
    
    return {
        "tiempo_inicio": time.strftime("%H:%M:%S", time.localtime(tiempo_inicio)),
        "tiempo_final": time.strftime("%H:%M:%S", time.localtime(time.time())),
        "duracion": f"{tiempo_total:.2f} segundos"
    }

# ------------------------------Quick No Sort Recursivo--------------------------------
def quicksort_iterative(punt_plays, year):
    comparator = PlayComparator()
    tiempo_inicio = time.time()
    
    def partition(arr, low, high):
        pivot = arr[high]
        i = low - 1
        
        for j in range(low, high):
            if comparator.compare(arr[j], pivot) <= 0:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1
    
    stack = []
    start = 0
    end = len(punt_plays) - 1
    
    stack.append(start)
    stack.append(end)
    
    while stack:
        end = stack.pop()
        start = stack.pop()
        
        p = partition(punt_plays, start, end)
        
        if p-1 > start:
            stack.append(start)
            stack.append(p - 1)
        
        if p+1 < end:
            stack.append(p + 1)
            stack.append(end)
    
    tiempo_total = time.time() - tiempo_inicio
    save_results_to_csv(punt_plays, "QUICK_ITERATIVO", year)
    
    return {
        "tiempo_inicio": time.strftime("%H:%M:%S", time.localtime(tiempo_inicio)),
        "tiempo_final": time.strftime("%H:%M:%S", time.localtime(time.time())),
        "duracion": f"{tiempo_total:.2f} segundos"
    }