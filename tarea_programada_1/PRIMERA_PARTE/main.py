from lector_data import LectorData  # Importa la clase para leer datos de archivos CSV
from sorting_algorithms import (  # Importa todos los algoritmos de ordenamiento
    bubble_sort,
    insertion_sort,
    mergesort_recursive,
    mergesort_iterative,
    quicksort_recursive,
    quicksort_iterative
)

def main():  # Función principal del programa
    print("=== PRIMERA PARTE - ANÁLISIS DE ALGORITMOS DE ORDENAMIENTO ===\n")  # Imprime título del programa
    
    years = range(2009, 2018)  # Define rango de años a procesar (2009-2017)
    
    algoritmos = {  # Crea un diccionario que asocia nombres de algoritmos con sus respectivas funciones
        "Bubble Sort": bubble_sort,  # Asocia el nombre "Bubble Sort" con la función bubble_sort
        "Insertion Sort": insertion_sort,  # Asocia el nombre "Insertion Sort" con la función insertion_sort
        "Merge Sort Iterativo": mergesort_iterative,  # Asocia el nombre "Merge Sort Iterativo" con la función mergesort_iterative
        "Merge Sort Recursivo": mergesort_recursive,  # Asocia el nombre "Merge Sort Recursivo" con la función mergesort_recursive
        "Quick Sort Iterativo": quicksort_iterative,  # Asocia el nombre "Quick Sort Iterativo" con la función quicksort_iterative
        "Quick Sort Recursivo": quicksort_recursive   # Asocia el nombre "Quick Sort Recursivo" con la función quicksort_recursive
    }
        
    for year in years:  # Itera sobre cada año en el rango definido
        print(f"\n=== Procesando año {year} ===")  # Imprime un mensaje indicando el año que está siendo procesado
        
        punts = LectorData(year).read_punts()  # Lee y filtra jugadas tipo punt. read_punts() filtra la informacion del archivo CSV y devuelve una lista
        print(f"Jugadas cargadas para {year}: {len(punts)}")  # Muestra cantidad de jugadas. {len(punts)} cuenta la cantidad de registros disponibles en punts
        
        for nombre, algoritmo in algoritmos.items():  # Itera sobre cada algoritmo. .items() es una característica de Python que permite iterar sobre los pares clave-valor de un diccionario.
            print(f"\nEjecutando {nombre} para {year}")  # Indica algoritmo actual
            punts_copy = punts.copy()  # Crea copia de jugadas para no modificar original. Es importante copiar los datos antes de pasarlos a un algoritmo porque algunos algoritmos modifican las listas directamente.
            
            stats = algoritmo(punts_copy, year)  # Ejecuta el algoritmo de ordenamiento y guarda las estadísticas retornadas
            
            # Imprime estadísticas de ejecución
            print(f"Tiempo inicio: {stats['tiempo_inicio']}")  # Hora de inicio
            print(f"Tiempo final: {stats['tiempo_final']}")  # Hora de finalización
            print(f"Duracion: {stats['duracion']}")  # Duración en segundos
            print(f"Comparaciones realizadas: {stats['comparaciones']}")  # Número de comparaciones
            print(f"Intercambios realizados: {stats['intercambios']}")  # Número de intercambios

# Verifica si el archivo se está ejecutando directamente. Cuando un archivo se ejecuta directamente, Python establece __name__ = "__main__".
# (__name__ determina si un archivo está siendo ejecutado directamente o si está siendo importado como un módulo en otro archivo).
# Cuando un archivo se importa como módulo, __name__ es el nombre del archivo. Si otro archivo importa main.py, __name__ será "main".
if __name__ == "__main__":
    main()  # Ejecuta la función principal