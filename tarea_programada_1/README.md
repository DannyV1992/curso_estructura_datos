# Tarea programada 1

## Descripción
Este proyecto implementa diferentes algoritmos de ordenamiento para procesar datos de jugadas tipo "punt" de la NFL, utilizando programación orientada a objetos en Python. El proyecto está dividido en dos partes principales.

## Estructura del proyecto
```
curso_estructura_datos/
└── tarea_programada_1/
    ├── .raw_data/               # Archivos CSV (pbp_2009.csv hasta pbp_2017.csv)
    ├── PRIMERA_PARTE/           # Implementación primera parte
    │   ├── archivos_ordenados/  # Resultados ordenados primera parte
    │   ├── punt_play.py
    │   ├── lector_data.py
    │   ├── sorting_algorithms.py
    │   └── main.py              # Archivo para ejecutar la primera parte
    └── SEGUNDA_PARTE/           # Implementación segunda parte
        ├── archivos_ordenados/  # Resultados ordenados segunda parte
        ├── punt_play.py
        ├── lector_data.py
        ├── play_comparator.py
        ├── sorting_algorithms.py
        └── main.py              # Archivo para ejecutar la segunda parte
```

## Características principales

### Primera parte
- Ordenamiento por yardas ganadas (descendente)
- Implementación de operadores de comparación (>, <, ==, >=, <=)
- Medición de tiempos, comparaciones e intercambios
- Algoritmos implementados:
  * Bubble Sort
  * Insertion Sort
  * Merge Sort (recursivo y no recursivo)
  * Quick Sort (recursivo y no recursivo)

### Segunda parte
- Ordenamiento por múltiples criterios:
  1. Fecha (ascendente)
  2. Cuarto (ascendente)
  3. Yardas ganadas (descendente)
  4. Hora (ascendente)
- Uso de PlayComparator para comparaciones
- Solo medición de tiempos de ejecución

## Requisitos
- Python 3.x
- Visual Studio Code
- No se requieren bibliotecas adicionales (solo biblioteca estándar de Python)

## Ejecución
Luego de clonar el repositorio y agregarlo en VS Code, dirijase a la terminal y ejecute los siguientes comandos:
1. Si desea ejecutar los archivos de la primera parte:
   ```
   cd tarea_programada_1
   cd PRIMERA_PARTE
   python main.py
   ```
2. Si desea ejecutar los archivos de la segunda parte:
   ```
   cd tarea_programada_1
   cd SEGUNDA_PARTE
   python main.py
   ```
3. Alternativamente puede dirijirse a los archivos `main.py` de la [primera parte](PRIMERA_PARTE/main.py) o de la [segunda parte](SEGUNDA_PARTE/main.py) y ejecutar directamente el codigo desde ahi.

Nota sobre navegación entre directorios:
- Si está en PRIMERA_PARTE y desea acceder a SEGUNDA_PARTE:
  ```
  cd ..
  cd SEGUNDA_PARTE
  ```
- Si está en SEGUNDA_PARTE y desea acceder a PRIMERA_PARTE:
  ```
  cd ..
  cd PRIMERA_PARTE
  ```

Los archivos CSV ya están incluidos en el repositorio dentro de la carpeta `.raw_data`, por lo que no es necesario descargarlos o agregarlos manualmente.

## Notas importantes
- Los archivos de salida se generan en las carpetas `archivos_ordenados` respectivas de cada directorio.
- El formato de salida es: "PARTE[1/2]-[ALGORITMO]-resultado-[AÑO].csv"
- Para la PRIMERA PARTE, es probable que el algoritmo de "Quick Sort Recursivo" genere un error y no se logre ejecutar debido a que se supera el límite máximo de recursión permitido en el programa (el cual es 1000 por defecto), por lo cual es un comportamiento esperado.

## Autor
Daniel Vásquez González