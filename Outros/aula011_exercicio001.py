import aula011

v = float(input("Qual o valor da moeda? R$"))
formatar = str(input("Quer formatar? [S/N]: ")).upper()[0]

while formatar != "S" and formatar != "N":
    print("Comando inválido! Tente novamente.")
    formatar = str(input("Quer formatar? [S/N]: ")).upper()[0]

if formatar == "S":
    f = True
else:
    if formatar == "N":
        f = False


acrescimo = aula011.aumentar(v, 10)
decrescimo = aula011.diminuir(v, 10)

valor = aula011.moeda(v)

if f:
    print(f"o valor {valor} com o acrescimo de 10% é {aula011.moeda(acrescimo)}")
    print(f"o valor {valor} com o decrescimo de 10% é {aula011.moeda(decrescimo)}")
    print(f"o dobro do {valor} é {aula011.moeda(aula011.dobro(v))}")
    print(f"a metade do {valor} é {aula011.moeda(aula011.metade(v))}")
else:
    print(f"o valor {valor} com o acrescimo de 10% é {aula011.moeda(acrescimo, f=False)}")
    print(f"o valor {valor} com o decrescimo de 10% é {aula011.moeda(decrescimo, f=False)}")
    print(f"o dobro do {valor} é {aula011.moeda(aula011.dobro(v), f=False)}")
    print(f"a metade do {valor} é {aula011.moeda(aula011.metade(v), f=False)}")