def bubble_sort(lista):
    for i in range(0, len(lista)):
        for j in range(0, len(lista)-1-i):
            if lista[j+1]<lista[j]:
                temp = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = temp
                print(lista) #descomente el print para ver la ejecucion

def selection_sort(lista):
    for i in range(0,len(lista)):
        min = i
        for j in range(i+1, len(lista)):
            if lista[j] < lista[min]:
                min = j
        temp = lista[i]
        lista[i] = lista[min]
        lista[min] = temp
        #print(lista)

def insertion_sort(lista):
    for i in range(1,len(lista)):
        v = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > v:
            lista[j+1] = lista[j]
            j = j - 1
        lista[j + 1] = v
        print(lista)