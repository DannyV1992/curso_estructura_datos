from datetime import datetime  # Importa datetime para manejar fechas y tiempos

class PlayComparator:
    def compare(self, play_a, play_b):  # Método que compara dos jugadas según múltiples criterios
        # 1. Comparar por fecha (ascendente)
        date_a = datetime.strptime(play_a.date, '%Y-%m-%d')  # Convierte string de fecha a objeto datetime para play_a
        date_b = datetime.strptime(play_b.date, '%Y-%m-%d')  # Convierte string de fecha a objeto datetime para play_b
        
        if date_a < date_b:  # Si la fecha de play_a es anterior
            return -1  # Indica que play_a es "menor" que play_b
        elif date_a > date_b:  # Si la fecha de play_b es anterior
            return 1  # Indica que play_a es "mayor" que play_b
            
        # 2. Si las fechas son iguales, comparar por cuarto (ascendente)
        if play_a.quarter < play_b.quarter:  # Si el cuarto de play_a es menor
            return -1  # Indica que play_a es "menor" que play_b
        elif play_a.quarter > play_b.quarter:  # Si el cuarto de play_b es menor
            return 1  # Indica que play_a es "mayor" que play_b
            
        # 3. Si el cuarto es igual, comparar por yardas (descendente)
        if play_a.yards_gained > play_b.yards_gained:  # Si las yardas de play_a son mayores (orden descendente)
            return -1  # Indica que play_a es "menor" que play_b
        elif play_a.yards_gained < play_b.yards_gained:  # Si las yardas de play_b son mayores
            return 1  # Indica que play_a es "mayor" que play_b
            
        # 4. Si las yardas son iguales, comparar por tiempo (ascendente)
        time_a = datetime.strptime(play_a.time, '%H:%M')  # Convierte string de tiempo a objeto datetime para play_a
        time_b = datetime.strptime(play_b.time, '%H:%M')  # Convierte string de tiempo a objeto datetime para play_b
        
        if time_a < time_b:  # Si el tiempo de play_a es anterior
            return -1  # Indica que play_a es "menor" que play_b
        elif time_a > time_b:  # Si el tiempo de play_b es anterior
            return 1  # Indica que play_a es "mayor" que play_b
            
        # Si todo es igual
        return 0  # Indica que las jugadas son iguales según todos los criterios
