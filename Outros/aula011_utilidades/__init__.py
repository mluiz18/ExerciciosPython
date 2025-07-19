def aumentar(n, a=0):
    novo_valor = n + (n * a)/100
    return novo_valor

def diminuir(n, d=0):
    novo_valor = n - (n * d) / 100
    return novo_valor

def dobro(n):
    return n * 2

def metade(n):
    return n / 2

def moeda(valor=0, moeda="R$", f=True):
    if f:
        return f"{moeda}{valor}"
    else:
        return valor