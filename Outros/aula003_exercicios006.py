numero = int(input("Digite um número: "))
razao = int(input("Digite um numero: "))
c = 1
termos_mostrados = 0

while c <= 10:
    print(numero)
    numero += razao
    c += 1
    termos_mostrados += 1

termos = int(input("Quantos termos a mais vc quer ver? "))
c = 1
while termos != 0:
    while c <= termos:
        print(numero)
        numero += razao
        c += 1
        termos_mostrados += 1
    termos = int(input("Quantos termos a mais vc quer ver? "))
    c = 1

print(f"Foram mostrados ao todo {termos_mostrados} termos.")