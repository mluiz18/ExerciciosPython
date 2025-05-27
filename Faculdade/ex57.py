def somador(vetor):
    soma = 0
    for i in range(len(vetor)):
        soma += vetor[i]

    return soma

vetor = [9,8,13,-5,29,31,81,18]
soma = somador(vetor)
print(soma)