def menu():
    print("-="*3, "SISTEMA DE TABUADA", "=-"*3)
    print(" 1 - Adição")
    print(" 2 - Subtração")
    print(" 3 - Multiplicação")
    print(" 4 - Divisão")
    print(" 5 - Sair do programa")

def tabuada_adicao(n):
    for i in range(1,11):
        print(f"{n} + {i} = {n+i}")

def tabuada_subtração(n):
    for i in range(n,n+11):
        print(f"{i} - {n} = {i - n}")

def tabuada_multiplicacao(n):
    for i in range(1,11):
        print(f"{n} x {i} = {n*i}")

def tabuada_divisao(numero):
    for i in range(1,11):
        print(f"{numero*i} / {numero} = {(numero*i)/numero}")

from time import sleep
while True:
    numero = int(input("Digite o número que quer operar: "))
    menu()
    opcao = int(input("Digite sua opção: "))

    while opcao != 1 and opcao != 2 and opcao != 3 and opcao != 4 and opcao != 5:
        print("Comando inválido! Tente novamente.")
        opcao = int(input("Digite sua opção: "))
    if opcao == 1:
        tabuada_adicao(numero)
    else:
        if opcao == 2:
            tabuada_subtração(numero)
        else:
            if opcao == 3:
                tabuada_multiplicacao(numero)
            else:
                if opcao == 4:
                    tabuada_divisao(numero)
                else:
                    if opcao == 5:
                        print("Finalizando o programa.")
                        sleep(0.5)
                        print("Finalizando o programa..")
                        sleep(0.5)
                        print("Finalizando o programa...")
                        sleep(0.5)
                        break
    print("-="*30)