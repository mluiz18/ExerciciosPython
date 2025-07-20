def menu():
    from time import sleep
    arq = "cursoemvideo.txt"

    print("-="*3, "MENU", "=-"*3)
    print("1 - Lista de pessoas")
    print("2 - Cadastrar nova pessoa")
    print("3 - Sair do Programa")
    while True:
        try:
            e = int(input("O que deseja fazer? "))
        except ValueError:
            print("Opção Inválida! Tente novamente.")
            continue
        else:
            sleep(0.2)
            while e <= 0 or e > 3:
                print("Opção inválida! Tente novamente.")
                e = int(input("O que deseja fazer? "))
            return e
