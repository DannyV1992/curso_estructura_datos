import os
import struct

class FileHandler:
    def __init__(self, base_path="data/segundaprogramada"):
        self.base_path = base_path
        self.main_file = os.path.join(base_path, "info.dat")
        self.record_size = 256  # Definimos un tamaño fijo para cada registro
        self.total_records = 750

    def initialize_main_file(self):
        """Crea el archivo info.dat si no existe con 750 registros vacíos"""
        if not os.path.exists(self.base_path):
            os.makedirs(self.base_path)
            
        if not os.path.exists(self.main_file):
            with open(self.main_file, 'wb') as file:
                # Escribimos registros vacíos
                empty_record = b'\0' * self.record_size
                for _ in range(self.total_records):
                    file.write(empty_record)
            return True
        return False

    def is_position_empty(self, position):
        """Verifica si una posición está vacía en info.dat"""
        with open(self.main_file, 'rb') as file:
            file.seek(position * self.record_size)
            data = file.read(self.record_size)
            return data.strip(b'\0') == b''

    def write_record(self, position, record_data):
        """Escribe un registro en una posición específica"""
        with open(self.main_file, 'r+b') as file:
            file.seek(position * self.record_size)
            # Aseguramos que el registro no exceda el tamaño fijo
            record_bytes = record_data.encode()[:self.record_size]
            record_bytes = record_bytes.ljust(self.record_size, b'\0')
            file.write(record_bytes)
