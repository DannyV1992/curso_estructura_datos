import time
import os

# ------------------------------Archivos de salida por año-------------------------------
def save_results_to_csv(punt_plays, algorithm_name, year):
    # Construir la ruta a la carpeta archivos_ordenados
    current_dir = os.path.dirname(os.path.abspath(__file__))  # os.path.abspath(__file__) obtiene la ruta absoluta del archivo actual y os.path.dirname() sube 1 nivel hasta tarea_programada_1
    output_dir = os.path.join(current_dir, "archivos_ordenados") # os.path.join() construye la ruta completa
        
    # Construir la ruta completa del archivo
    # output_filename = f"PARTE1-{algorithm_name}-resultado.csv" # Para cuando se quiere agrupar todos los años en un mismo archivo
    output_filename = f"PARTE1_{algorithm_name}_resultado_{year}.csv"
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
    # Inicializamos contadores
    comparaciones = 0
    intercambios = 0
    
    # Registramos tiempo inicial
    tiempo_inicio = time.time()
    
    n = len(punt_plays)
    for i in range(0, n):
        for j in range(0, n-1-i):
            # Incrementamos contador de comparaciones
            comparaciones += 1
            
            # Usamos los operadores sobrescritos en PuntPlay
            if punt_plays[j+1] < punt_plays[j]:
                # Incrementamos contador de intercambios
                intercambios += 1
                
                # Realizamos el intercambio
                temp = punt_plays[j]
                punt_plays[j] = punt_plays[j+1]
                punt_plays[j+1] = temp
    
    # Calculamos tiempo total
    tiempo_total = time.time() - tiempo_inicio

    # Guardar resultados
    # save_results_to_csv(punt_plays, "BUBBLE")
    save_results_to_csv(punt_plays, "BUBBLE", year)

    # Retornamos estadísticas
    return {
        "tiempo_inicio": time.strftime("%H:%M:%S", time.localtime(tiempo_inicio)),
        "tiempo_final": time.strftime("%H:%M:%S", time.localtime(time.time())),
        "duracion": f"{tiempo_total:.2f} segundos",
        "comparaciones": comparaciones,
        "intercambios": intercambios
    }

# ------------------------------Insertion Sort--------------------------------
def insertion_sort(punt_plays, year):
    comparaciones = 0
    intercambios = 0
    tiempo_inicio = time.time()
    
    for i in range(1, len(punt_plays)):
        v = punt_plays[i]
        j = i - 1
        while j >= 0:
            comparaciones += 1
            if punt_plays[j] > v:
                punt_plays[j + 1] = punt_plays[j]
                intercambios += 1
                j = j - 1
            else:
                break
        punt_plays[j + 1] = v
    
    tiempo_total = time.time() - tiempo_inicio

    # Guardar resultados
    save_results_to_csv(punt_plays, "INSERTION", year)

    return {
        "tiempo_inicio": time.strftime("%H:%M:%S", time.localtime(tiempo_inicio)),
        "tiempo_final": time.strftime("%H:%M:%S", time.localtime(time.time())),
        "duracion": f"{tiempo_total:.2f} segundos",
        "comparaciones": comparaciones,
        "intercambios": intercambios
    }

# ------------------------------Merge Sort Recursivo--------------------------------
def merge(left, right, comparaciones, intercambios):
    result = []
    i, j = 0, 0
    
    while i < len(left) and j < len(right):
        comparaciones += 1
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            intercambios += 1
            
    result.extend(left[i:])
    result.extend(right[j:])
    return result, comparaciones, intercambios

def mergesort_recursive(punt_plays, year):
    tiempo_inicio = time.time()
    comparaciones = 0
    intercambios = 0
    
    def _mergesort(l):
        nonlocal comparaciones, intercambios
        if len(l) < 2:
            return l[:]
        else:
            middle = len(l) // 2
            left = _mergesort(l[:middle])
            right = _mergesort(l[middle:])
            merged, comp, inter = merge(left, right, comparaciones, intercambios)
            comparaciones = comp
            intercambios = inter
            return merged
    
    punt_plays[:] = _mergesort(punt_plays)
    tiempo_total = time.time() - tiempo_inicio

    # Guardar resultados
    save_results_to_csv(punt_plays, "MERGE_RECURSIVO", year)
    
    return {
        "tiempo_inicio": time.strftime("%H:%M:%S", time.localtime(tiempo_inicio)),
        "tiempo_final": time.strftime("%H:%M:%S", time.localtime(time.time())),
        "duracion": f"{tiempo_total:.2f} segundos",
        "comparaciones": comparaciones,
        "intercambios": intercambios
    }

# ------------------------------Merge No Sort Recursivo--------------------------------
def mergesort_iterative(punt_plays, year):
    tiempo_inicio = time.time()
    comparaciones = 0
    intercambios = 0
    n = len(punt_plays)
    width = 1
    
    def merge_nr(a, l, m, r):
        nonlocal comparaciones, intercambios
        n1 = m - l + 1
        n2 = r - m
        L = [a[l + i] for i in range(n1)]
        R = [a[m + 1 + i] for i in range(n2)]
        
        i, j, k = 0, 0, l
        while i < n1 and j < n2:
            comparaciones += 1
            if L[i] <= R[j]:
                a[k] = L[i]
                i += 1
            else:
                a[k] = R[j]
                j += 1
                intercambios += 1
            k += 1
            
        while i < n1:
            a[k] = L[i]
            i += 1
            k += 1
        while j < n2:
            a[k] = R[j]
            j += 1
            k += 1
    
    while width < n:
        l = 0
        while l < n:
            r = min(l + (width * 2 - 1), n - 1)
            m = min(l + width - 1, n - 1)
            merge_nr(punt_plays, l, m, r)
            l += width * 2
        width *= 2
    
    tiempo_total = time.time() - tiempo_inicio

    # Guardar resultados
    save_results_to_csv(punt_plays, "MERGE_ITERATIVO", year)

    return {
        "tiempo_inicio": time.strftime("%H:%M:%S", time.localtime(tiempo_inicio)),
        "tiempo_final": time.strftime("%H:%M:%S", time.localtime(time.time())),
        "duracion": f"{tiempo_total:.2f} segundos",
        "comparaciones": comparaciones,
        "intercambios": intercambios
    }

# ------------------------------Quick Sort Recursivo--------------------------------
def quicksort_recursive(punt_plays, year):
    tiempo_inicio = time.time()
    comparaciones = 0
    intercambios = 0
    
    def partition(arr, low, high):
        nonlocal comparaciones, intercambios
        pivot = arr[high]
        i = low - 1
        
        for j in range(low, high):
            comparaciones += 1
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                intercambios += 1
        
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        intercambios += 1
        return i + 1
    
    def _quicksort(arr, low, high):
        if low < high:
            pi = partition(arr, low, high)
            _quicksort(arr, low, pi - 1)
            _quicksort(arr, pi + 1, high)
    
    _quicksort(punt_plays, 0, len(punt_plays) - 1)
    
    tiempo_total = time.time() - tiempo_inicio

    # Guardar resultados
    save_results_to_csv(punt_plays, "QUICK_RECURSIVO", year)

    return {
        "tiempo_inicio": time.strftime("%H:%M:%S", time.localtime(tiempo_inicio)),
        "tiempo_final": time.strftime("%H:%M:%S", time.localtime(time.time())),
        "duracion": f"{tiempo_total:.2f} segundos",
        "comparaciones": comparaciones,
        "intercambios": intercambios
    }

# ------------------------------Quick No Sort Recursivo--------------------------------
def quicksort_iterative(punt_plays, year):
    tiempo_inicio = time.time()
    comparaciones = 0
    intercambios = 0
    
    def partition(arr, l, h):
        nonlocal comparaciones, intercambios
        x = arr[h]
        i = l - 1
        
        for j in range(l, h):
            comparaciones += 1
            if arr[j] <= x:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                intercambios += 1
        
        arr[i + 1], arr[h] = arr[h], arr[i + 1]
        intercambios += 1
        return i + 1
    
    l = 0
    h = len(punt_plays) - 1
    size = h - l + 1
    stack = [0] * size
    top = -1
    
    top += 1
    stack[top] = l
    top += 1
    stack[top] = h
    
    while top >= 0:
        h = stack[top]
        top -= 1
        l = stack[top]
        top -= 1
        
        p = partition(punt_plays, l, h)
        
        if p - 1 > l:
            top += 1
            stack[top] = l
            top += 1
            stack[top] = p - 1
            
        if p + 1 < h:
            top += 1
            stack[top] = p + 1
            top += 1
            stack[top] = h
    
    tiempo_total = time.time() - tiempo_inicio

    # Guardar resultados
    save_results_to_csv(punt_plays, "QUICK_ITERATIVO", year)

    return {
        "tiempo_inicio": time.strftime("%H:%M:%S", time.localtime(tiempo_inicio)),
        "tiempo_final": time.strftime("%H:%M:%S", time.localtime(time.time())),
        "duracion": f"{tiempo_total:.2f} segundos",
        "comparaciones": comparaciones,
        "intercambios": intercambios
    }