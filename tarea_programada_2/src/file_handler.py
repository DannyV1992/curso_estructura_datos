import os # Importa módulo para manejo de rutas y directorios
import pickle # Importa módulo para serialización de objetos
from punt_play import PuntPlay # Importa la clase PuntPlay definida anteriormente

class FileHandler: # Define la clase para manejar archivos
    def __init__(self): # Constructor de la clase
        self.base_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'processed_data') # Define ruta base para archivos procesados
        self.main_file = os.path.join(self.base_path, 'info.dat') # Define ruta del archivo principal info.dat
        
    def initialize_main_file(self): # Método para inicializar el archivo principal
        os.makedirs(self.base_path, exist_ok=True) # Crea el directorio si no existe
        
        if not os.path.exists(self.main_file): # Verifica si el archivo principal no existe
            with open(self.main_file, 'wb') as file: # Abre archivo en modo escritura binaria
                # Crear 750 registros vacíos usando pickle
                for _ in range(750): # Itera 750 veces
                    pickle.dump(None, file) # Escribe None como registro vacío
    
    def write_record(self, position, punt_play): # Método para escribir un registro en posición específica
        records = self._read_all_records() # Obtiene todos los registros actuales
        
        if records[position] is None: # Comprueba si la posición está vacía
            records[position] = punt_play # Asigna el nuevo objeto a la posición
            
            with open(self.main_file, 'wb') as file: # Abre archivo en modo escritura binaria
                for record in records: # Itera sobre todos los registros
                    pickle.dump(record, file) # Escribe cada registro
            return True # Retorna éxito
        return False # Retorna falso si posición ocupada
    
    def write_collision(self, position, punt_play): # Método para escribir colisiones
        collision_file = os.path.join(self.base_path, f"{position}-col.dat") # Crea nombre archivo colisiones
        
        with open(collision_file, 'ab') as file: # Abre archivo colisiones en modo append binario
            pickle.dump(punt_play, file) # Escribe el objeto al final del archivo
    
    def read_record(self, position): # Método para leer registro y sus colisiones
        records = self._read_all_records() # Obtiene todos los registros
        main_record = records[position] # Obtiene el registro principal en la posición
        
        collisions = [] # Inicializa lista vacía para colisiones
        collision_file = os.path.join(self.base_path, f"{position}-col.dat") # Define ruta archivo colisiones
        
        if os.path.exists(collision_file): # Si existe archivo de colisiones
            with open(collision_file, 'rb') as file: # Abre archivo colisiones en modo lectura
                while True: # Loop infinito
                    try: # Intenta leer un registro
                        collisions.append(pickle.load(file)) # Agrega colisión a lista
                    except EOFError: # Captura fin de archivo
                        break # Sale del loop
        
        return main_record, collisions # Retorna tupla con registro principal y lista de colisiones
    
    def _read_all_records(self): # Método privado para leer todos los registros
        records = [] # Inicializa lista de registros
        
        if os.path.exists(self.main_file): # Si existe el archivo principal
            with open(self.main_file, 'rb') as file: # Abre archivo en modo lectura binaria
                for _ in range(750): # Itera 750 veces
                    try: # Intenta leer un registro
                        record = pickle.load(file) # Carga el registro
                        records.append(record) # Agrega registro a la lista
                    except EOFError: # Captura fin de archivo
                        break # Sale del loop
        
        while len(records) < 750: # Mientras no haya 750 registros
            records.append(None) # Agrega None para completar
            
        return records # Retorna lista completa de registros