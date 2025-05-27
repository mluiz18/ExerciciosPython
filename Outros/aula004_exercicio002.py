while True:
    numero = int(input("Você quer ver a tabuada de qual número? "))
    if numero < 0:
        print("-" * 40)
        print("Número inválido, encerrando programa...")
        print("-" * 40)
        break
    else:
        print(f"Tabuada do {numero}")
        print("-" * 15)
        c = 1
        while c <= 10:
            print(f"{numero} x {c} = {numero * c}")
            c += 1
        print("-" * 15)