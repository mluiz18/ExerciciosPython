numero = int(input("Digite o número: "))
divisivel = 0
c = 1
for i in range(numero+1):
    if numero % c == 0:
        divisivel += 1
    c += 1

if divisivel > 2:
    print(f"O Numero {numero} não é primo!")
else:
    print(f"O Número {numero} é primo!")