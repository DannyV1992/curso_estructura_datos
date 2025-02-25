class PuntPlay:
    def __init__(self, game_id, away_team, home_team, yards_gained, quarter, date, time):  # Constructor que inicializa los atributos de la jugada
        self.game_id = int(game_id)  # Convierte y almacena el ID del juego como entero
        self.teams = f"{away_team} @ {home_team}"  # Crea string con formato "equipo visitante @ equipo local"
        self.yards_gained = float(yards_gained) if yards_gained else 0.0  # Convierte yardas a float, si es None asigna 0.0
        self.quarter = int(quarter) if quarter else 0  # Convierte el cuarto a entero, si es None asigna 0
        self.date = date  # Almacena la fecha de la jugada
        self.time = time  # Almacena la hora de la jugada