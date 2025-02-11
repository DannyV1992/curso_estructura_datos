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

"""
def test_classes():
    # 1. Prueba de la clase PuntPlay
    print("=== Prueba de PuntPlay ===")
    play1 = PuntPlay("2009_01", "NYJ", "NE", 45.0, 1, "2009-09-01", "14:55")
    play2 = PuntPlay("2009_02", "GB", "CHI", 38.0, 2, "2009-09-01", "13:22")
    
    print(f"Play 1: {play1}")
    print(f"Play 2: {play2}")
    print(f"Play 1 > Play 2: {play1 > play2}")  # Debería ser True
    print(f"Play 1 < Play 2: {play1 < play2}")  # Debería ser False
    print(f"Play 1 == Play 2: {play1 == play2}\n")  # Debería ser False

    # 2. Prueba de LectorData
    print("=== Prueba de LectorData ===")
    lector = LectorData(2009)  # Probando año 2009
    punts = lector.read_punts()
    
    print(f"Número de jugadas tipo punt encontradas: {len(punts)}")
    if punts:
        print("\nPrimeras 3 jugadas encontradas:")
        for i in range(min(3, len(punts))):
            print(f"Jugada {i+1}: {punts[i]}")

if __name__ == "__main__":
    test_classes()

from sorting_algorithms import bubble_sort
"""

"""
def test_bubble_sort():
    print("\n=== Prueba de Bubble Sort ===")
    lector = LectorData(2009)
    punts = lector.read_punts()
    
    if punts:
        print(f"Ordenando {len(punts)} jugadas...")
        stats = bubble_sort(punts)
        
        print("\nEstadísticas:")
        print(f"Tiempo inicio: {stats['tiempo_inicio']}")
        print(f"Tiempo final: {stats['tiempo_final']}")
        print(f"Duración: {stats['duracion']}")
        print(f"Comparaciones: {stats['comparaciones']}")
        print(f"Intercambios: {stats['intercambios']}")
        
        print("\nPrimeras 3 jugadas después de ordenar:")
        for i in range(min(3, len(punts))):
            print(f"Jugada {i+1}: {punts[i]}")

if __name__ == "__main__":
    test_bubble_sort()
"""

# .........................................

def test_sorting_algorithms():
    # Inicializar el lector con año específico
    lector = LectorData(2017)
    punts = lector.read_punts()
    
    if punts:
        # Definir algoritmos a probar
        algoritmos = {
            #"Bubble Sort": bubble_sort,
            #"Insertion Sort": insertion_sort,
            #"Merge Sort Iterativo": mergesort_iterative,
            #"Merge Sort Recursivo": mergesort_recursive,
            #"Quick Sort Iterativo": quicksort_iterative,
            "Quick Sort Recursivo": quicksort_recursive
        }
        
        # Probar cada algoritmo
        for nombre, algoritmo in algoritmos.items():
            print(f"\n=== Probando {nombre} ===")
            punts_copy = punts.copy()  # Crear copia para cada prueba
            
            # Ejecutar algoritmo y obtener estadísticas
            stats = algoritmo(punts_copy, 2017)  # Añadir el año como parámetro
            
            # Mostrar resultados
            print("\nEstadisticas:")
            print(f"Tiempo inicio: {stats['tiempo_inicio']}")
            print(f"Tiempo final: {stats['tiempo_final']}")
            print(f"Duracion: {stats['duracion']}")
            print(f"Comparaciones: {stats['comparaciones']}")
            print(f"Intercambios: {stats['intercambios']}")
            print("-" * 50)

if __name__ == "__main__":
    test_sorting_algorithms()
    