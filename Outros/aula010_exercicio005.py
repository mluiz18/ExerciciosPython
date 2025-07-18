def notas(*notas, sit=False):
    """
    Função que calcula a quantidade, a maior, a menor, a média, e se você quiser a situação. Independente da quantidade de notas
    :param notas: Notas, quantas você quiser.
    :param sit: se quer mostrar a situação
    :return: dicionario
    """
    resultado = dict()
    resultado["quantidade"] = len(notas)

    maior = notas[0]
    for i in range(len(notas)):
        if notas[i] > maior:
            maior = notas[i]
    resultado["maior"] = maior

    menor = notas[0]
    for i in range(len(notas)):
        if notas[i] < menor:
            menor = notas[i]
    resultado["menor"] = menor

    s = 0
    for n in notas:
        s += n
    media = s/len(notas)
    resultado["média"] = media

    if sit:
        if media < 0:
            resultado["situação"] = "como você fez isso?"
        else:
            if media < 1:
                resultado["situação"] = "deplorável, melhore!"
            else:
                if media < 5:
                    resultado["media"] = "Ruim"
                else:
                    if media < 7:
                        resultado["situação"] = "Aceitavel, mas pode melhorar!"
                    else:
                        if media < 10:
                            resultado["situação"] = "Muito bom!"
    return resultado


resp = notas(5.5,2.5,10,6.5,sit=True)
print(resp)