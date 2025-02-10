import csv
import os
from punt_play import PuntPlay

class LectorData:
    def __init__(self, year):
        self.filename = f"pbp_{year}.csv" # Selecciona dinamicamente el nombre del archivo .csv basado en el año ingresado
        self.base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # os.path.abspath(__file__) obtiene la ruta absoluta del archivo actual y os.path.dirname() sube dos niveles (desde PRIMERA_PARTE hasta tarea_programada_1)
        self.file_path = os.path.join(self.base_path, ".raw_data", self.filename) # os.path.join() construye la ruta completa
        # print(f"Ruta: {self.file_path}") # Debug para ver la ruta completa

    def read_punts(self):
        punt_plays = []
        
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                csv_reader = csv.DictReader(file)
                
                for row in csv_reader:
                    if (row['PlayType'] == 'Punt' and 'FUMBLE' not in row.get('desc', '').upper()):
                        
                        play = PuntPlay(
                            game_id=row['GameID'],
                            away_team=row['AwayTeam'],
                            home_team=row['HomeTeam'],
                            yards_gained=row['Yards.Gained'],
                            quarter=row['qtr'],
                            date=row['Date'],
                            time=row['time']
                        )
                        punt_plays.append(play)
                        
        except FileNotFoundError:
            print(f"Error: No se encontró el archivo {self.filename}")
        except Exception as e:
            print(f"Error al procesar el archivo {self.filename}: {str(e)}")
            
        return punt_plays
