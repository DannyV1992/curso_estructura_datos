class HashFunction:
    def __init__(self, table_size=750): # Constructor con tamaño de tabla predeterminado
        self.table_size = table_size # Almacena el tamaño de la tabla hash
        
    def calculate_hash(self, punt_play: object) -> int: # Método para calcular hash
        date_str = punt_play.date.replace('-', '') # Elimina guiones de la fecha
        quarter_str = str(punt_play.quarter) # Convierte cuarto a string
        local_team_str = punt_play.teams.split(' @ ')[1] # Obtiene equipo local
        combined_str = date_str + quarter_str + local_team_str # Combina strings
        
        hash_value = 0 # Inicializa el valor hash
        for char in combined_str: # Itera sobre cada carácter
            hash_value = (hash_value * 31 + ord(char)) % self.table_size # Aplica función hash
            
        return hash_value # Retorna posición hash calculada


