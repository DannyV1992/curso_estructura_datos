# Tarea programada 2

## Descripción
Este proyecto implementa un sistema de almacenamiento de registros utilizando una estrategia de hash. El sistema lee datos de jugadas de fútbol americano y los almacena en archivos binarios, utilizando una función hash para determinar su ubicación.

## Estructura del proyecto
```
curso_estructura_datos/
└── tarea_programada_2/
    ├── src/
    │   ├── __init__.py
    │   ├── file_handler.py
    │   ├── hash_function.py
    │   ├── menu_handler.py
    │   ├── punt_play.py
    │   └── main.py             # Archivo para ejecutar el modelo
    ├── data/
    │   ├── .raw_data/          # Archivos CSV originales
    │   └── processed_data/     # Archivos binarios generados
    └── README.md
```

## Componentes principales
- `file_handler.py`: maneja la lectura y escritura de archivos binarios
- `hash_function.py`: implementa la función hash para distribuir los registros
- `menu_handler.py`: gestiona la interfaz de usuario
- `punt_play.py`: define la clase para los registros de jugadas
- `main.py`: punto de entrada del programa

## Funcionalidades
1. **Cargar datos**: lee archivos CSV y almacena registros usando función hash
2. **Buscar datos**: busca registros por posición (0-749)
3. **Manejo de colisiones**: almacena colisiones en archivos separados

## Requisitos
- Python 3.x
- Solo utiliza módulos de la Python Standard Library
- No requiere instalación de paquetes adicionales

## Uso
1. Ejecutar `main.py`
2. Seleccionar opción del menú:
   - 1: Cargar datos
   - 2: Buscar datos
   - 3: Salir

## Archivos de datos
- Entrada: archivos CSV ubicados en `curso_estructura_datos/data/.raw_data/`
- Salida: archivos .dat ubicados en `curso_estructura_datos/data/processed_data/`
  - `info.dat`: archivo principal (750 registros)
  - `xxx-col.dat`: archivos de colisiones

## Autor
Daniel Vásquez González
