lista1 = [5, 8, 3, 10, 2]
def bubble_sort(lista):
    n = len(lista)
    for j in range(n-1):
        for i in range(n - 1):
            if lista[i] > lista[i+1]:
                lista[i], lista[i+1] = lista[i+1], lista[i]
bubble_sort(lista1)

#complexidade de tempo O(n^2)
#complexidade de espaçao O(n)