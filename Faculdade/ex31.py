n = int(input("Digite um valor: "))
if n <= 0:
    print("Numero inválido!")
else:
    f = 1
    for i in range(1, n+1):
        f = f*i
    print(f"O Fatorial de {n}! é {f}.")