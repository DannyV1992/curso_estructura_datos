from punt_play import PuntPlay
from lector_data import LectorData
from sorting_algorithms import (
    bubble_sort,
    insertion_sort,
    mergesort_recursive,
    mergesort_iterative,
    quicksort_recursive,
    quicksort_iterative
)

def main():
    print("=== PRIMERA PARTE - ANALISIS DE ALGORITMOS DE ORDENAMIENTO ===\n")
    
    # Lista de años a procesar
    years = range(2009, 2018)
    
    # Diccionario de algoritmos a ejecutar
    algoritmos = {
        "Bubble Sort": bubble_sort,
        "Insertion Sort": insertion_sort,
        "Merge Sort Iterativo": mergesort_iterative,
        "Merge Sort Recursivo": mergesort_recursive,
        "Quick Sort Iterativo": quicksort_iterative,
        #"Quick Sort Recursivo": quicksort_recursive
    }
        
    # Procesar cada año por separado
    for year in years:
        print(f"=== Procesando anio {year} ===")
        
        # Cargar datos del año
        lector = LectorData(year)
        punts = lector.read_punts()
        print(f"Jugadas cargadas para {year}: {len(punts)}")
        
        # Ejecutar cada algoritmo
        for nombre, algoritmo in algoritmos.items():
            print(f"\nEjecutando {nombre} para {year}")
            punts_copy = punts.copy()
            
            stats = algoritmo(punts_copy, year)  # Pasamos el año como parámetro
            
            print(f"Tiempo inicio: {stats['tiempo_inicio']}")
            print(f"Tiempo final: {stats['tiempo_final']}")
            print(f"Duracion: {stats['duracion']}")
            print(f"Comparaciones realizadas: {stats['comparaciones']}")
            print(f"Intercambios realizados: {stats['intercambios']}")

if __name__ == "__main__":
    main()
