import csv  # Importa el módulo csv para leer archivos CSV
import os   # Importa el módulo os para manejo de rutas de archivos
import platform  # Importa platform para identificar el sistema operativo
from punt_play import PuntPlay  # Importa la clase PuntPlay del archivo punt_play.py

class LectorData:
    def __init__(self, year):  # Constructor que recibe el año como parámetro
        self.filename = f"pbp_{year}.csv"  # Construye el nombre del archivo CSV basado en el año
        self.base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # Obtiene la ruta base subiendo dos niveles desde el archivo actual
        self.file_path = os.path.join(self.base_path, ".raw_data", self.filename)  # Construye la ruta completa al archivo CSV
        
        # Determina el sistema operativo y establece la ruta alternativa
        self.alt_path = "/data/primeraprogramada" if platform.system() == "Darwin" else "c:\\data\\primeraprogramada"  # Darwin es el kernel de MacOS
        self.alt_file_path = os.path.join(self.alt_path, self.filename)  # Construye la ruta alternativa completa

    def read_punts(self):  # Método para leer y filtrar jugadas tipo punt
        punt_plays = []  # Lista para almacenar las jugadas filtradas
        file_read = False  # Flag para controlar si se logró leer el archivo
        
        # Primero intenta leer desde la ruta principal
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:  # Intenta abrir el archivo en la ruta principal
                csv_reader = csv.DictReader(file)  # Crea un lector CSV que mapea filas a diccionarios
                punt_plays = self._process_csv(csv_reader)  # Procesa el CSV y obtiene las jugadas
                file_read = True  # Marca que se logró leer el archivo
                print(f"Archivo leído exitosamente desde: {self.file_path}")
                
        except FileNotFoundError:  # Si no encuentra el archivo en la ruta principal
            print(f"No se encontró el archivo en {self.file_path}, intentando ruta alternativa...")
            
        # Si no se pudo leer el archivo, intenta con la ruta alternativa
        if not file_read:
            try:
                with open(self.alt_file_path, 'r', encoding='utf-8') as file:  # Intenta abrir el archivo en la ruta alternativa
                    csv_reader = csv.DictReader(file)  # Crea un nuevo lector CSV
                    punt_plays = self._process_csv(csv_reader)  # Procesa el CSV
                    print(f"Archivo leído exitosamente desde: {self.alt_file_path}")
                    
            except FileNotFoundError:  # Si tampoco encuentra el archivo en la ruta alternativa
                print(f"Error: no se encontró el archivo {self.filename} en ninguna ubicación")
            except Exception as e:  # Maneja cualquier otro error
                print(f"Error al procesar el archivo {self.filename}: {str(e)}")
                
        return punt_plays  # Retorna la lista de jugadas filtradas

    def _process_csv(self, csv_reader):  # Método auxiliar para procesar el CSV
        punt_plays = []
        for row in csv_reader:  # Itera sobre cada fila del archivo
            if row['PlayType'] == 'Punt' and 'FUMBLE' not in row['desc'].upper():  # Filtra solo jugadas tipo Punt sin FUMBLE
                # Crea un nuevo objeto PuntPlay con los datos de la fila
                play = PuntPlay(
                    game_id=row['GameID'],  # ID del juego
                    away_team=row['AwayTeam'],  # Equipo visitante
                    home_team=row['HomeTeam'],  # Equipo local
                    yards_gained=row['Yards.Gained'],  # Yardas ganadas
                    quarter=row['qtr'],  # Cuarto
                    date=row['Date'],  # Fecha
                    time=row['time']  # Hora
                )
                punt_plays.append(play)  # Agrega la jugada a la lista
        return punt_plays