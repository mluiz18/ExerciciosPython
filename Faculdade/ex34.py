soma_valores = 0
quantidade_valor = 0
valor = int(input("Digite um valor: "))

while valor >= 1:
    soma_valores += valor
    quantidade_valor += 1
    valor = int(input("Digite um valor: "))
if quantidade_valor > 0:
    print(f"A média dos valores digitados é {soma_valores/quantidade_valor}")