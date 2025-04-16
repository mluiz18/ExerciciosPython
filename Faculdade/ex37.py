n1 = int(input("Digite um valor: "))
n2 = int(input("Digite um valor: "))
maior_numero = n1
menor_numero = n2

if n2 > maior_numero:
    maior_numero = n2
    menor_numero = n1

for i in range(maior_numero+1):
    print(menor_numero)
    menor_numero += 1
    if menor_numero == maior_numero+1:
        break