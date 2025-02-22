import os # Importa módulo para manejo de rutas y directorios
from file_handler import FileHandler # Importa clase FileHandler
from hash_function import HashFunction # Importa clase HashFunction
from punt_play import PuntPlay # Importa clase PuntPlay

class MenuHandler:
    def __init__(self): # Constructor vacío
        self.file_handler = FileHandler() # Instancia FileHandler
        self.hash_function = HashFunction() # Instancia HashFunction
        # self.raw_data_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', '.raw_data') # Construye la ruta completa para los archivos CSV
        self.base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # Obtiene la ruta base subiendo dos niveles desde el archivo actual
        self.raw_data_path = os.path.join(self.base_path, "data", ".raw_data") # Define ruta a archivos CSV
    def display_menu(self): # Método para mostrar menú
        print("\nMenú principal:")
        print("1. Cargar datos")
        print("2. Buscar datos")
        print("3. Salir")
    
    def load_data(self): # Método para cargar datos
        self.file_handler.initialize_main_file() # Inicializa archivo principal
        
        for filename in os.listdir(self.raw_data_path): # Itera sobre archivos CSV
            if filename.startswith('PARTE1_BUBBLE_resultado_'): # Verifica si es archivo válido
                with open(os.path.join(self.raw_data_path, filename), 'r') as file: # Abre archivo CSV
                    next(file) # Salta encabezado
                    
                    for line in file: # Lee línea por línea
                        game_id, teams, yards_gained, quarter, date, time = line.strip().split(',') # Extrae datos
                        
                        punt_play = PuntPlay(game_id, *teams.split(' @ '), float(yards_gained), int(quarter), date, time) # Crea objeto PuntPlay
                        position = self.hash_function.calculate_hash(punt_play) # Calcula posición hash
                        
                        if not self.file_handler.write_record(position, punt_play): # Si posición está ocupada
                            self.file_handler.write_collision(position, punt_play) # Escribe colisión
    
    def search_data(self): # Método para buscar datos
        position = int(input("Ingrese la posición (0-749): ")) # Pide posición al usuario
        
        main_record, collisions = self.file_handler.read_record(position) # Lee registro principal y colisiones
        
        if main_record is None: # Si no hay registro principal
            print("Registro vacío.")
        else: # Si hay registro principal
            print("Registro Principal:")
            print(main_record)
            
            if collisions: # Si hay colisiones
                print("\nColisiones:")
                for collision in collisions:
                    print(collision)
    
    def run(self): # Método para ejecutar menú
        while True: # Loop infinito
            self.display_menu() # Muestra menú
            
            option = input("Ingrese una opción: ") # Pide opción al usuario
            
            if option == '1': # Opción Cargar Datos
                self.load_data()
            elif option == '2': # Opción Buscar Datos
                self.search_data()
            elif option == '3': # Opción Salir
                break
            else: # Opción inválida
                print("Opción inválida. Por favor, intente nuevamente.")
