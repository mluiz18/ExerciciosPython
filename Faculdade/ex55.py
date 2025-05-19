def menor_elemento(vetor):
    menor = 0
    for i in range(len(vetor)):
        if i == 0:
            menor = vetor[i]
        else:
            if vetor[i] < menor:
                menor = vetor[i]
        
    return menor

vetor = [9,8,13,-5,29,31,81,18]
print(menor_elemento(vetor))