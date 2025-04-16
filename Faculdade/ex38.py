n = int(input("Digite um valor: "))

for i in range(n):
    valor = int(input("Digite um valor: "))
    print(f"O Valor lido foi {valor}")
    f = 1
    for x in range(1, n+1):
        f = f*x
    print(f"O Fatorial de {valor}! é {f}.")