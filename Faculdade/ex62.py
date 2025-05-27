def substitui_negativos_por_zero(vetor):
    for i in range(len(vetor)):
        if vetor[i] < 0:
            vetor [i] = 0

    return vetor

vetor = [9,8,13,-5,29,31,-81,18]
novo_vetor = substitui_negativos_por_zero(vetor)
print(novo_vetor)