class PuntPlay:
    def __init__(self, game_id, away_team, home_team, yards_gained, quarter, date, time):  # Constructor que inicializa los atributos de la jugada
        self.game_id = int(game_id)  # Convierte y almacena el ID del juego como entero
        self.teams = f"{away_team} @ {home_team}"  # Crea string con formato "equipo visitante @ equipo local"
        self.yards_gained = float(yards_gained) if yards_gained else 0.0  # Convierte yardas a float, si es None asigna 0.0
        self.quarter = int(quarter) if quarter else 0  # Convierte el cuarto a entero, si es None asigna 0
        self.date = date  # Almacena la fecha de la jugada
        self.time = time  # Almacena la hora de la jugada

    # Sobreescritura de operadores, esto permite definir cómo se comportará un objeto cuando se utilizan operadores comunes (como +, -, <, >, ==). Retorna un valor booleano

    def __eq__(self, other):  # Operador de igualdad (==)
        return self.yards_gained == other.yards_gained  # Compara si las yardas ganadas son iguales

    def __lt__(self, other):  # Operador menor que (<)
        return self.yards_gained < other.yards_gained  # Compara si las yardas ganadas son menores

    def __gt__(self, other):  # Operador mayor que (>)
        return self.yards_gained > other.yards_gained  # Compara si las yardas ganadas son mayores

    def __le__(self, other):  # Operador menor o igual que (<=)
        return self.yards_gained <= other.yards_gained  # Compara si las yardas ganadas son menores o iguales

    def __ge__(self, other):  # Operador mayor o igual que (>=)
        return self.yards_gained >= other.yards_gained  # Compara si las yardas ganadas son mayores o iguales
    
    def __str__(self):  # Método que convierte el objeto PuntPlay a string con formato CSV
        return f"{self.game_id},{self.teams},{self.yards_gained},{self.quarter},{self.date},{self.time}"  # Retorna string con atributos separados por comas
