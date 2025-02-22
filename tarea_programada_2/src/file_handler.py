import os # Importa módulo para manejo de rutas y directorios
import struct # Importa módulo para empaquetar/desempaquetar datos binarios
from punt_play import PuntPlay # Importa la clase PuntPlay definida anteriormente

class FileHandler: # Define la clase para manejar archivos
    def __init__(self): # Constructor de la clase
        
        self.base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # Obtiene la ruta base subiendo dos niveles desde el archivo actual
        self.base_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'processed_data') # Define ruta base para archivos procesados
        self.main_file = os.path.join(self.base_path, 'info.dat') # Define ruta del archivo principal info.dat
        self.record_size = 256 # Define tamaño fijo para cada registro en bytes
        
    def initialize_main_file(self): # Método para inicializar el archivo principal
        os.makedirs(self.base_path, exist_ok=True) # Crea el directorio si no existe
        
        if not os.path.exists(self.main_file): # Verifica si el archivo principal no existe
            with open(self.main_file, 'wb') as file: # Abre archivo en modo escritura binaria
                empty_record = b'\0' * self.record_size # Crea registro vacío con bytes nulos
                for _ in range(750): # Itera 750 veces
                    file.write(empty_record) # Escribe registro vacío
    
    def write_record(self, position: int, punt_play: PuntPlay) -> bool: # Método para escribir un registro en posición específica
        record_data = self._serialize_punt_play(punt_play) # Convierte PuntPlay a bytes
        
        with open(self.main_file, 'rb+') as file: # Abre archivo en modo lectura/escritura binaria
            file.seek(position * self.record_size) # Mueve puntero a la posición calculada
            current_data = file.read(self.record_size) # Lee datos actuales en esa posición
            
            if current_data.strip(b'\0') == b'': # Verifica si la posición está vacía
                file.seek(position * self.record_size) # Regresa puntero a la posición inicial
                file.write(record_data) # Escribe los nuevos datos
                return True # Retorna éxito
            return False # Retorna falso si posición ocupada
    
    def write_collision(self, position: int, punt_play: PuntPlay): # Método para escribir colisiones
        collision_file = os.path.join(self.base_path, f"{position}-col.dat") # Crea nombre archivo colisiones
        record_data = self._serialize_punt_play(punt_play) # Convierte PuntPlay a bytes
        
        with open(collision_file, 'ab') as file: # Abre archivo colisiones en modo append binario
            file.write(record_data) # Escribe datos al final del archivo
    
    def read_record(self, position: int) -> tuple[PuntPlay, list[PuntPlay]]: # Método para leer registro y sus colisiones
        main_record = None # Inicializa registro principal como None
        collisions = [] # Inicializa lista vacía para colisiones
        
        with open(self.main_file, 'rb') as file: # Abre archivo principal en modo lectura binaria
            file.seek(position * self.record_size) # Mueve puntero a posición calculada
            data = file.read(self.record_size) # Lee datos en esa posición
            if data.strip(b'\0'): # Si hay datos (no está vacío)
                main_record = self._deserialize_punt_play(data) # Convierte bytes a PuntPlay
        
        collision_file = os.path.join(self.base_path, f"{position}-col.dat") # Define ruta archivo colisiones
        if os.path.exists(collision_file): # Si existe archivo de colisiones
            with open(collision_file, 'rb') as file: # Abre archivo colisiones en modo lectura
                while True: # Loop infinito
                    data = file.read(self.record_size) # Lee un registro
                    if not data: # Si no hay más datos
                        break # Sale del loop
                    collisions.append(self._deserialize_punt_play(data)) # Agrega colisión a lista
        
        return main_record, collisions # Retorna tupla con registro principal y lista de colisiones
    
    def _serialize_punt_play(self, punt_play: PuntPlay) -> bytes: # Método privado para convertir PuntPlay a bytes
        data = struct.pack('i', punt_play.game_id) # Empaqueta ID del juego
        data += punt_play.teams.encode('utf-8').ljust(50) # Empaqueta equipos con padding
        data += struct.pack('f', punt_play.yards_gained) # Empaqueta yardas ganadas
        data += struct.pack('i', punt_play.quarter) # Empaqueta número de cuarto
        data += punt_play.date.encode('utf-8').ljust(15) # Empaqueta fecha con padding
        data += punt_play.time.encode('utf-8').ljust(10) # Empaqueta tiempo con padding
        return data.ljust(self.record_size, b'\0') # Retorna datos con padding total
    
    def _deserialize_punt_play(self, data: bytes) -> PuntPlay: # Método privado para convertir bytes a PuntPlay
        game_id = struct.unpack('i', data[:4])[0] # Desempaqueta ID del juego
        teams = data[4:54].decode('utf-8').strip() # Desempaqueta y limpia equipos
        away_team, home_team = teams.split(' @ ') # Separa equipos visitante y local
        yards_gained = struct.unpack('f', data[54:58])[0] # Desempaqueta yardas ganadas
        quarter = struct.unpack('i', data[58:62])[0] # Desempaqueta número de cuarto
        date = data[62:77].decode('utf-8').strip() # Desempaqueta y limpia fecha
        time = data[77:87].decode('utf-8').strip() # Desempaqueta y limpia tiempo
        
        return PuntPlay(game_id, away_team, home_team, yards_gained, quarter, date, time) # Retorna nuevo objeto PuntPlay