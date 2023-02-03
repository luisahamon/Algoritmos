#Algoritmo de Busca Binária
#Algoritmo Recursivo que usa a estratégia dividir para conquistar
#desvantagem: só funciona em vetores ordenados
import time
inicio = time.time()
def busca_binária(v, p, r, elemento):
    #condição de existência da recursividade
    if p <= r:
        meio = (p+r) // 2
        if elemento > v[meio]:
            return busca_binária(v, meio+1,r,elemento)
        elif elemento < v[meio]:
            return busca_binária(v, meio-1,r,elemento)
        else:
            return meio
    return -1
vetor = list(range(0,1000))
chave = 999
posição = busca_binária(vetor, 0, len(vetor)-1,chave)
print(posição)
fim = time.time()
tempo = (fim - inicio) * 1000
print('O tempo de execução foi de %0.2f ms' % tempo)
#o tempo de execução para 1000 elemento foi 1 ms