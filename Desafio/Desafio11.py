numero1 = int(input("Digite um número: "))
numero2 = int(input("Digite um número: "))

if numero1 > numero2:
    print(f"O Número {numero1} é maior que o número {numero2}")
else:
    if numero2 > numero1:
        print(f"O Número {numero2} é maior que o número {numero1}")
    else:
        print("Os números digitados são iguais!")