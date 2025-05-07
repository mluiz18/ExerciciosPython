n1 = int(input("Digite um número: "))
n2 = int(input("Digite um número: "))
escolha = 0

while escolha != 5:
    print("[1] somar")
    print("[2] multiplicar")
    print("[3] maior")
    print("[4] novos numeros")
    print("[5] sair")
    escolha = int(input("Digite sua ação: "))
    print("---------------------------------")

    if escolha == 1:
        soma = n1 + n2
        print(f"{n1} + {n2} = {soma}")
        print("-----------------------")
    else:
        if escolha == 2:
            multiplicacao = n1*n2
            print(f"{n1} x {n2} = {multiplicacao}")
            print("------------------------------")
        else:
            if escolha == 3:
                maior = n1
                if n2 > maior:
                    maior = n2
                print(f"O Maior numero digitado foi {maior}.")
                print("---------------------------------------")
            else:
                if escolha == 4:
                    n1 = int(input("Digite um número: "))
                    n2 = int(input("Digite um número: "))
                    print("-----------------------------")