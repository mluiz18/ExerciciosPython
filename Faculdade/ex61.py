def media_de_vetor(vetor):
    soma = 0
    for i in range(len(vetor)):
        soma += vetor[i]

    if len(vetor) == 0:
        media = 0
    else:
        media = soma / len(vetor)

    return media

vetor = [9,8,13,-5,29,31,81,18]
media = media_de_vetor(vetor)
print(media)