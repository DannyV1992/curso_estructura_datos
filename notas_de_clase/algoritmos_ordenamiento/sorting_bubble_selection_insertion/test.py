"""

a = []

# por aqui llenaron la lista. 
# este ciclo es lineia 
for elemento in lista:
    # ...
    # ...


# en cambio si solo tengo un ciclo y estoy cambiado HACIA LA MITAD 
#lo que recorro, es O(log n)

a = 0
b = len(lista)

while a<b:
    mitad = lista((a + b)/2)
    if condicion:
        b = (a + b)/2
    else:
        a = (a + b)/2


si tengo 2 ciclos anidados
y el de afuera influeye en el de adentro y el adentro va disminuyendo, 
eso O(n log n)

for i in range(1,10000)
  for j in range(10000/i,100000)

si no hay influencia
for i in range(.....):
   for j in range(....
                  
                  O(n ^ 2)
"""