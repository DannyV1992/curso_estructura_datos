from single_linked_list import single_linked_list
from nodo import nodo

mi_lista = single_linked_list()
un_nodo = nodo(44)
mi_lista.imprimir()
mi_lista.insert(un_nodo)
print("-----")
mi_lista.imprimir()
un_nodo = nodo(33)
mi_lista.insert(un_nodo)
un_nodo = nodo(25)
mi_lista.insert(un_nodo)
un_nodo = nodo(66)
mi_lista.insert(un_nodo)
print("-----")
mi_lista.imprimir()