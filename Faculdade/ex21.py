ano = int(input("Digite o ano do veiculo: "))
peso = int(input("Digite o peso do veiculo: "))

if ano < 1970:
    if peso < 1200:
        print("Classe 1")
        print("Taxa de registro: US$16,50")
    elif peso >= 1200 and peso <= 1700:
        print("Classe 2")
        print("Taxa de registro: US$25,50")
    elif peso > 1700:
        print("Classe 3")
        print("Taxa de registro: US$46,50")
elif ano >= 1971 and ano <= 1979:
    if peso < 1200:
        print("Classe 4")
        print("Taxa de registro: US$27,00")
    elif peso >= 1200 and peso <= 1700:
        print("Classe 5")
        print("Taxa de registro: US$30,50")
    elif peso > 1700:
        print("Classe 6")
        print("Taxa de registro: US$52,50")
elif ano >= 1980:
    if peso < 1600:
        print("Classe 7")
        print("Taxa de registro: US$19,50")
    elif peso >= 1600:
        print("Classe 8")
        print("Taxa de registro US$ 55,50")