valores = []
for x in range(5):
    valores.append(int(input(f"Digite um valor para a posição {x}: ")))

menor = valores[0]
maior = valores[0]
posicao_maior = []
posicao_menor = []


for i in range(len(valores)):
    if valores[i] > maior:
        maior = valores[i]
    else:
        if valores[i] < menor:
            menor = valores[i]


for x in range(len(valores)):
    if valores[x] == maior:
        posicao_maior.append(x)
    else:
        if valores[x] == menor:
            posicao_menor.append(x)

print(f"Você digitou os valores: {valores}")
print(f"O Maior valor da lista é {maior}, nas posições: {posicao_maior}")
print(f"O Menor valor da lista é {menor}, nas posições:: {posicao_menor}")