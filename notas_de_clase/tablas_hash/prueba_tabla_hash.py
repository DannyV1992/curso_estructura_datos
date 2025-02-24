from tabla_hash import Tabla_Hash
# Ejemplo sencillo funcion hash
def function_hash_1(obetjo, max):
    return len(obetjo) % max

def function_hash_2(objeto, max):
    parte_fraccional = (len(objeto) * 0.6154985126518) % 1
    key = int(max * parte_fraccional)
    return key

mi_tabla = Tabla_Hash(10)
mi_tabla.display_table()
print("===================")

mi_tabla.insert(1 , ["uno", 2, "tres"])
mi_tabla.display_table()
print("===================")

mi_tabla.insert(9, 90)
mi_tabla.display_table()
print("===================")

try:
    mi_tabla.insert(11, 90)
except:
    print("la llave 11 esta fuera de rango")
print("===================")

elemento1 = [2,3,4,5,6]
mi_tabla.insert(function_hash_1(elemento1, 10), elemento1)
mi_tabla.display_table()
print("===================")

elemento2 = [5,32,7,956,66,78]
mi_tabla.insert(function_hash_2(elemento2, 10), elemento2)
mi_tabla.display_table()
