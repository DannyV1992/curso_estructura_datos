from punt_play import PuntPlay  # Importa la clase PuntPlay para representar jugadas tipo "punt"
from lector_data import LectorData  # Importa la clase LectorData para leer y filtrar datos de archivos CSV
from play_comparator import PlayComparator  # Importa la clase PlayComparator para realizar comparaciones personalizadas
from sorting_algorithms import (  # Importa los algoritmos de ordenamiento implementados
    bubble_sort,
    insertion_sort,
    mergesort_recursive,
    mergesort_iterative,
    quicksort_recursive,
    quicksort_iterative
)

def main():  # Define la función principal del programa
    print("=== SEGUNDA PARTE - ANALISIS DE ALGORITMOS DE ORDENAMIENTO ===\n")  # Imprime un título indicando el propósito del programa
    
    years = range(2009, 2018)  # Define un rango de años a procesar (2009-2017 inclusive)
    
    algoritmos = {  # Crea un diccionario que asocia nombres de algoritmos con sus respectivas funciones
        "Bubble Sort": bubble_sort,  # Asocia el nombre "Bubble Sort" con la función bubble_sort
        "Insertion Sort": insertion_sort,  # Asocia el nombre "Insertion Sort" con la función insertion_sort
        "Merge Sort Iterativo": mergesort_iterative,  # Asocia el nombre "Merge Sort Iterativo" con la función mergesort_iterative
        "Merge Sort Recursivo": mergesort_recursive,  # Asocia el nombre "Merge Sort Recursivo" con la función mergesort_recursive
        "Quick Sort Iterativo": quicksort_iterative,  # Asocia el nombre "Quick Sort Iterativo" con la función quicksort_iterative
        #"Quick Sort Recursivo": quicksort_recursive  # Comentado: Quick Sort recursivo no se ejecutará en esta configuración
    }
    
    for year in years:  # Itera sobre cada año en el rango definido
        print(f"=== Procesando anio {year} ===")  # Imprime un mensaje indicando el año que está siendo procesado
        
        lector = LectorData(year)  # Crea instancia para leer datos del año. LectorData() recibe un año como parametro para identificar cual archivo CSV debe abrir
        punts = lector.read_punts()  # Lee y filtra jugadas tipo punt. read_punts() filtra la informacion del archivo CSV y devuelve una lista
        print(f"Jugadas cargadas para {year}: {len(punts)}")  # Muestra cantidad de jugadas. {len(punts)} cuenta la cantidad de registros disponibles en punts
        
        for nombre, algoritmo in algoritmos.items():  # Itera sobre cada algoritmo. .items() es una característica de Python que permite iterar sobre los pares clave-valor de un diccionario.
            print(f"\nEjecutando {nombre} para {year}")  # Indica algoritmo actual
            punts_copy = punts.copy()  # Crea copia de jugadas para no modificar original. Es importante copiar los datos antes de pasarlos a un algoritmo porque algunos algoritmos modifican las listas directamente.
            
            stats = algoritmo(punts_copy, year)  # Ejecuta el algoritmo de ordenamiento y guarda las estadísticas retornadas
            
            # Imprime las estadísticas de ejecución del algoritmo
            print(f"Tiempo inicio: {stats['tiempo_inicio']}")  # Muestra la hora en que comenzó la ejecución del algoritmo
            print(f"Tiempo final: {stats['tiempo_final']}")  # Muestra la hora en que terminó la ejecución del algoritmo
            print(f"Duracion: {stats['duracion']}")  # Muestra cuánto tiempo tomó ejecutar el algoritmo

# Verifica si este archivo se está ejecutando directamente (no importado como módulo)
# Cuando un archivo se ejecuta directamente, Python establece __name__ = "__main__".
# Si este archivo es importado como módulo en otro archivo, __name__ será igual al nombre del archivo ("main").
if __name__ == "__main__":
    main()  # Llama a la función principal para iniciar el programa

