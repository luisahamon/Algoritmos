lista1 = [66,7,0,45,88,2,20]

def quicksort(lista, inicio = 0, fim = None):
    if fim == None:
        fim = len(lista) - 1
    if inicio < fim:
        p = partition(lista, inicio, fim)
        quicksort(lista,inicio, p-1)
        quicksort(lista, p+1, fim)
def partition(lista, inicio, fim):
    pivo = lista[fim]
    i = inicio
    for j in range(inicio, fim):
        if lista[j] <= pivo:
            lista[j], lista[i] = lista[i], lista[j]
            i = i + 1
    lista[i], lista[fim] = lista[fim], lista[i]
    return i

quicksort(lista1)
print(lista1)