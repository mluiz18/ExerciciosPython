def ordenador(vetor):
    for i in range(len(vetor)):
        for j in range(i, len(vetor)):
            if vetor[j] < vetor[i]:
                aux = vetor[i]
                vetor[i] = vetor[j]
                vetor[j] = aux

    return vetor

vetor = [9,8,13,-5,29,31,81,18]
print(ordenador(vetor))