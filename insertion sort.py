lista1 = [18, 20, 5, 4, 0, 2]
def insertion_sort(lista):
    n = len(lista)
    for i in range(1, n):
        chave = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > chave:
            lista[j + 1] = lista[j]
            j = j - 1
        lista[j + 1] = chave
insertion_sort(lista1)
print(lista1)

#complexidade de tempo O(n^2)
#complexidade de espaçao O(n)