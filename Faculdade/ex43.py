valores = []

for i in range(10):
    valor = int(input("Digite um valor: "))
    valores.append(valor)

for x in range(len(valores)):
    if valores[x] < 0:
        print(valores[x])