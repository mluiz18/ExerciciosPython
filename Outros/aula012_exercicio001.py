def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print("Erro! Digite um valor inteiro válido")
            continue
        except KeyboardInterrupt:
            print("O Usuário preferiu não digitar!")
        else:
            return n

def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print("Erro! Digite um valor inteiro válido")
            continue
        else:
            return n


n = leiaInt("Digite um número: ")
print(f"Você digitou o número {n}")
f = leiaFloat("Digite um número: ")
print(f"Você digitou o número {f}")