def pertencente_ao_vetor(vetor, valor):
    achou = False
    for i in range(len(vetor)):
        if valor == vetor[i]:
            achou = True

    return achou
vetor = [9,8,13,-5,29,31,81,18]
numero = int(input("Digite um número: "))
pertece = pertencente_ao_vetor(vetor, numero)

if pertece:
    print("Achou")
else:
    print("Não achou")