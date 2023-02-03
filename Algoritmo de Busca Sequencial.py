#Algoritmo de Busca Sequencial
#Buscamos um elemento no vetor procurando indice por indice
import time
antes = time.time()
vetor = list(range(0,1000))
def busca_sequencial(v,x):
    i = 0
    while i < len(v):
        if v[i] == x:
            return i
        i += 1
    return -1
posição = busca_sequencial(vetor, 1000) 
if posição >= 0:
    print('O elemento foi encontrado na posição: %d' % (posição))
else:
    print('O elemento não foi encontrado')
depois = time.time()
total = (depois - antes) * 1000
print('O tempo total gasto foi de %0.2f ms' % total)
# em uma lista de 100 itens o tempo é de 1 ms
# em uma lista de 1000 itens o tempo é de 103.52 ms
