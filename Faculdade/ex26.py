numero1 = float(input("Digite um número: "))
numero2 = float(input("Digite um número: "))


print("--- Escolha sua ação ---")
print("[1] Adição")
print("[2] Multiplicação")
print("[3] Divisão")
codigo = int(input())

if codigo == 1:
    print(f"O Resultado da soma é {numero1+numero2}")
else:
    if codigo == 2:
        print(f"O Resultado da multiplicação é {numero1*numero2}")
    else:
        if codigo == 3:
            print(f"O Resultado da divisão é {numero1/numero2}")
        else:
            print("Código inválido")