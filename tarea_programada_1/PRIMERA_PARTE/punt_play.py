class PuntPlay:
    def __init__(self, game_id, away_team, home_team, yards_gained, quarter, date, time):
        self.game_id = int(game_id)
        self.teams = f"{away_team} @ {home_team}"
        self.yards_gained = float(yards_gained) if yards_gained else 0.0
        self.quarter = int(quarter) if quarter else 0
        self.date = date
        self.time = time

    def __eq__(self, other):
        return self.yards_gained == other.yards_gained

    def __lt__(self, other):
        return self.yards_gained < other.yards_gained

    def __gt__(self, other):
        return self.yards_gained > other.yards_gained

    def __le__(self, other):
        return self.yards_gained <= other.yards_gained

    def __ge__(self, other):
        return self.yards_gained >= other.yards_gained

    def __str__(self):
        return f"{self.game_id},{self.teams},{self.yards_gained},{self.quarter},{self.date},{self.time}"
