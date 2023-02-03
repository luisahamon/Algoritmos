#Algoritmo de Busca Sequencial com Sentinela
#adicionando uma sentinela diminuimos o tempo de execução do algoritmo 
import time
antes = time.time()
vetor = list(range(0,1000))
def busca_sequencial_sentinela(v,x):
    i = 0
    v.append(x) #adicionando uma sentinela
    while v[i] != x:
        i += 1
    if i == len(v) -1:
        return -1
    return i
x = 1000
posição = busca_sequencial_sentinela(vetor, x) 
if posição >= 0:
    print('O elemento foi encontrado na posição: %d' % (posição))
else:
    print('O elemento não foi encontrado')
depois = time.time()
total = (depois - antes) * 1000
print('O tempo total gasto foi de %0.2f ms' % total)
#com 1000 elementos o tempo foi 0.99 ms