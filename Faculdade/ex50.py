valor = int(input("Digite um valor: "))
vetor = [10, 0, -1, -3, 5, 8, -2, -4, 7, 9]

for i in range(len(vetor)):
    if valor == vetor[i]:
        print(f"O Número {valor} pertence ao vetor de inteiros: {vetor}")
    else:
        print(f"O Número {valor} NÃO pertence ao vetor de inteiros: {vetor}")