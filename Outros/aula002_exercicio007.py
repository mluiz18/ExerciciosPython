numero = int(input("digite um numero: "))
isNumeroPrimo = False

for x in range(1,numero+1):
    print(x)
    if numero / x == 1 or numero / x == numero:
        isNumeroPrimo = True
    else:
        isNumeroPrimo = False

print(f"o número {numero} é primo? {isNumeroPrimo}")
