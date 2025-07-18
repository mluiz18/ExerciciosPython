import aula011

v = float(input("Qual o valor da moeda? R$"))

acrescimo = aula011.aumentar(v, 10)
decrescimo = aula011.diminuir(v, 10)

print(acrescimo)
print(decrescimo)
print(aula011.dobro(v))
print(aula011.metade(v))