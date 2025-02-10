from datetime import datetime

class PlayComparator:
    def compare(self, play_a, play_b):
        # 1. Comparar por fecha (ascendente)
        date_a = datetime.strptime(play_a.date, '%Y-%m-%d')
        date_b = datetime.strptime(play_b.date, '%Y-%m-%d')
        
        if date_a < date_b:
            return -1
        elif date_a > date_b:
            return 1
            
        # 2. Si las fechas son iguales, comparar por cuarto (ascendente)
        if play_a.quarter < play_b.quarter:
            return -1
        elif play_a.quarter > play_b.quarter:
            return 1
            
        # 3. Si el cuarto es igual, comparar por yardas (descendente)
        if play_a.yards_gained > play_b.yards_gained:
            return -1
        elif play_a.yards_gained < play_b.yards_gained:
            return 1
            
        # 4. Si las yardas son iguales, comparar por tiempo (descendente)
        time_a = datetime.strptime(play_a.time, '%H:%M')
        time_b = datetime.strptime(play_b.time, '%H:%M')
        
        if time_a > time_b:
            return -1
        elif time_a < time_b:
            return 1
            
        # Si todo es igual
        return 0
