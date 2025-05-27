numero = int(input("Digite um número: "))
f = 1
c = numero

if numero < 0:
    print("Número inválido")
else:
    if numero == 0:
        print("1")
    else:
        while c > 0:
            f *= c
            c -= 1

print(f)