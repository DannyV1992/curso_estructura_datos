class HashFunction:
    def __init__(self, table_size=750): # Constructor con tamaño de tabla predeterminado
        self.table_size = table_size # Almacena el tamaño de la tabla hash
        
    def calculate_hash(self, punt_play): # Método para calcular hash
        date_str = punt_play.date.replace('/', '') # Elimina guiones de la fecha
        quarter_str = str(punt_play.quarter) # Convierte cuarto a string
        local_team_str = punt_play.teams.split(' @ ')[1] # Obtiene equipo local
        combined_str = date_str + quarter_str + local_team_str # Combina strings
        
        hash_value = 0 # Inicializa el valor hash
        for char in combined_str: # Itera sobre cada carácter
            hash_value = (hash_value * 31 + ord(char)) % self.table_size # Aplica función hash. ord(char) extrae el código ASCII
            
        return hash_value # Retorna posición hash calculada

'''
La manera en la que esta funcion hash opera es la siguiente:

1. Toma tres datos de la jugada:
   - La fecha (`date_str`): elimina las barras (/) para tener solo números y estandarizar el formato para crear una cadena de caracteres más consistente para el cálculo
   - El cuarto (`quarter_str`): lo convierte a texto
   - El equipo local (`local_team_str`): extrae el equipo que aparece después de "@"

2. Combina estos tres valores en una sola cadena (`combined_str`). Por ejemplo, si tenemos:
   - Fecha: "02/25/2025" → "02252025"
   - Cuarto: 3 → "3"
   - Equipo local: "DET"
   
   La cadena combinada sería: "022520253DET"

3. Inicializa un valor hash en 0
4. Para cada carácter en la cadena combinada:
   - Multiplica el hash actual por 31 (un número primo que ayuda a distribuir mejor los valores)
   - Suma el valor ASCII del carácter actual (por ejemplo, 'A' = 65)
   - Aplica el operador módulo (%) con el tamaño de la tabla (750) para mantener el resultado dentro del rango 0-749

    Por lo tanto para 022520253DET, la formula hash se veria como lo siguiente:
       
       El valor ASCII de cada carácter es:
            '0': 48
            '2': 50
            '5': 53
            '2': 50
            '0': 48
            '2': 50
            '5': 53
            '3': 51
            'D': 68
            'E': 69
            'T': 84
        
        Aplicando la fórmula al ejemplo anterior se vería de esta manera::
            - hash_value = 0
            - hash_value = (0 * 31 + 48) % 750 = 48
            - hash_value = (48 * 31 + 50) % 750 = 1538 % 750 = 38
            - hash_value = (38 * 31 + 53) % 750 = 1231 % 750 = 481
            - hash_value = (481 * 31 + 50) % 750 = 14961 % 750 = 711
            - hash_value = (711 * 31 + 48) % 750 = 22089 % 750 = 339
            - hash_value = (339 * 31 + 50) % 750 = 10559 % 750 = 559
            - hash_value = (559 * 31 + 53) % 750 = 17382 % 750 = 132
            - hash_value = (132 * 31 + 51) % 750 = 4143 % 750 = 393
            - hash_value = (393 * 31 + 68) % 750 = 12251 % 750 = 251
            - hash_value = (251 * 31 + 69) % 750 = 7850 % 750 = 100
            - hash_value = (100 * 31 + 84) % 750 = 3184 % 750 = 434

        Por lo tanto, el valor hash final para "022520253DET" es 434.

Este método, conocido como "polinomial rolling hash", es eficiente porque:
- Considera la posición de cada carácter (los primeros caracteres tienen más peso)
- Usa un multiplicador primo (31) que reduce colisiones
- Distribuye los valores de manera más uniforme en la tabla hash

El resultado final es un número entre 0 y 749 que indica dónde se almacenará la jugada en el archivo principal.
'''