def fatorial(n,show=False):
    """
    Calcula o fatorial e mostra na tela, podendo ou não, mostrar o calculo
    :param n: Número fatorial
    :param show: Valor booleano, para mostrar na tela
    :return: fatorial
    """
    f = 1
    for i in range(n):
        f *= i+1

    return f

numero = int(input("Numero: "))
s = str(input("Mostrar calculo: ")).upper()[0]
print(f"{numero}! = ", end="")
if s == "S":
    for i in range(numero):
        n = numero-i
        if n == 1:
            print(end=f"1 = {fatorial(numero,show=True)}")
        else:
            print(n, end=" x ")
else:
    print(f"{fatorial(numero,show=False)}")