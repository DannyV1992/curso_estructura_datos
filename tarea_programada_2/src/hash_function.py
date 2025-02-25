import hashlib # Importa módulo para funciones hash

class HashFunction:
    def __init__(self): # Constructor vacío
        pass
    
    def calculate_hash(self, punt_play: object) -> int: # Método para calcular hash
        date_str = punt_play.date.replace('-', '') # Elimina guiones de la fecha
        quarter_str = str(punt_play.quarter) # Convierte cuarto a string
        local_team_str = punt_play.teams.split(' @ ')[1] # Obtiene equipo local
        
        combined_str = date_str + quarter_str + local_team_str # Combina strings
        hash_object = hashlib.md5(combined_str.encode()) # Crea objeto hash MD5
        hash_hex = hash_object.hexdigest() # Obtiene hash en hexadecimal
        
        # Convierte hash hexadecimal a entero y lo reduce a 750 posiciones
        hash_int = int(hash_hex, 16) % 750
        
        return hash_int # Retorna posición hash calculada