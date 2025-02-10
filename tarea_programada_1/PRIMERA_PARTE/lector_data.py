import csv  # Importa el módulo csv para leer archivos CSV
import os   # Importa el módulo os para manejo de rutas de archivos
from punt_play import PuntPlay  # Importa la clase PuntPlay del archivo punt_play.py

class LectorData:
    def __init__(self, year):  # Constructor que recibe el año como parámetro
        self.filename = f"pbp_{year}.csv"  # Construye el nombre del archivo CSV basado en el año
        self.base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # Obtiene la ruta base subiendo dos niveles desde el archivo actual
        self.file_path = os.path.join(self.base_path, ".raw_data", self.filename)  # Construye la ruta completa al archivo CSV

    def read_punts(self):  # Método para leer y filtrar jugadas tipo punt
        punt_plays = []  # Lista para almacenar las jugadas filtradas
        
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:  # Abre el archivo CSV en modo lectura
                csv_reader = csv.DictReader(file)  # Crea un lector CSV que mapea filas a diccionarios
                
                for row in csv_reader:  # Itera sobre cada fila del archivo
                    if (row['PlayType'] == 'Punt' and 'FUMBLE' not in row.get('desc', '').upper()): # Filtra solo jugadas tipo Punt que no contengan FUMBLE
                        
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
                        punt_plays.append(play)  # Agrega la jugada a la list
                        
        except FileNotFoundError:  # Maneja error si no encuentra el archivo
            print(f"Error: No se encontró el archivo {self.filename}")
        except Exception as e:  # Maneja cualquier otro error
            print(f"Error al procesar el archivo {self.filename}: {str(e)}")
            
        return punt_plays  # Retorna la lista de jugadas filtradas

