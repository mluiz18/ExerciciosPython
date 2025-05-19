def maior_elemento(vetor):
    maior = 0
    for i in range(len(vetor)):
        if i == 0:
            maior = vetor[i]
        else:
            if vetor[i] > maior:
                maior = vetor[i]

    return maior

vetor = [9,8,13,-5,29,31,81,18]

print(maior_elemento(vetor))