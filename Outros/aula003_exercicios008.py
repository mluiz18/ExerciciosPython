numero = int(input("Digite um numero [999 para parar]: "))
soma = 0
c = 0
while numero != 999:
    soma += numero
    c += 1
    numero = int(input("Digite um numero [999 para parar]: "))
print(f"Você digitou {c} numeros, a soma entre eles é de {soma}")
