def calculadora_de_troco(tc):
    v = tc
    notas100 = 0
    notas50 = 0
    notas20 = 0
    notas10 = 0
    notas5 = 0
    notas2 = 0

    while v > 0:
        if v - 100 >= 0:
            notas100 += 1
            v -= 100
        else:
            if v - 50 >= 0:
                notas50 += 1
                v -= 50
            else:
                if v - 20 >= 0:
                    notas20 += 1
                    v -= 20
                else:
                    if v - 10 >= 0:
                        notas10 += 1
                        v -= 10
                    else:
                        if v - 5 >= 0:
                            notas5 += 1
                            v -= 5
                        else:
                            if v - 2 >= 0:
                                notas2 += 1
                                v -= 2
                            continue

    print(f"Notas de 100: {notas100}")
    print(f"Notas de 50: {notas50}")
    print(f"Notas de 20: {notas20}")
    print(f"Notas de 10: {notas10}")
    print(f"Notas de 5: {notas5}")
    print(f"Notas de 2: {notas2}")

valor = float(input("Digite o valor da compra: "))
valorPago = float(input("Digite o valor pago: "))
troco = valorPago - valor

if troco == 0:
    print("Sem troco necessário!")
else:
    if troco < 0:
        print(f"O Valor pago (R${valorPago}) foi menor do que o cobrado (R${valor})")
    else:
        calculadora_de_troco(troco)
