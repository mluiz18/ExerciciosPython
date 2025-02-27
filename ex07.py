qw = int(input("Digite a quantidade de quilowats gasto: "))
tQw = qw*0.12
qwICMS = tQw + (tQw * 18/100)
print(f"O Valor a ser pago será de R${qwICMS}")