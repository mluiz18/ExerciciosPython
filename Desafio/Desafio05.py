#Busca Binaria

def busca_binaria(x,vetor):
    menor = 0
    maior = len(vetor) - 1
    while menor <= maior:
        metade = int((menor+maior)/2)
        palpite = vetor[metade]
        if palpite == x:
            return metade
        if palpite > x:
            maior = metade - 1
        else:
            menor = metade + 1
    return None

n = [1,3,5,7,9]
print(busca_binaria(9,n))