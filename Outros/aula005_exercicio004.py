valor1 = int(input("Digite um valor: "))
valor2 = int(input("Digite um valor: "))
valor3 = int(input("Digite um valor: "))
valor4 = int(input("Digite um valor: "))

valores_gerados = valor1,valor2,valor3,valor4
numeronove = 0

for x in range(len(valores_gerados)):
    if valores_gerados[x] == 9:
        numeronove += 1

posição_primeiro_tres = valores_gerados.index(3)

pares = []
for i in range(len(valores_gerados)):
    if valores_gerados[i] % 2 == 0:
        pares.append(valores_gerados[i])

print(f"O Valor 9 apareceu {numeronove} vezes!")
print(f"O 3 aparece primeiro na posição {posição_primeiro_tres}")
print(f"Os números pares escritos foram: {pares}")