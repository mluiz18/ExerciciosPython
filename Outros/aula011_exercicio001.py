import aula011

v = float(input("Qual o valor da moeda? "))
ac = float(input("Qual valor acionar a moeda? "))
dc = float(input("Qual valor remover da moeda? "))

acrescimo = aula011.aumentar(v, ac)
decrescimo = aula011.diminuir(v, dc)

print(f"{v} + {ac} = {acrescimo}")
print(f"{v} - {dc} = {decrescimo}")
print(f"{v} * 2 = {aula011.dobro(v)}")
print(f"{v} / 2 = {aula011.metade(v)}")