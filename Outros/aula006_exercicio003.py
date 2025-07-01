valores = []
for x in range(5):
    valor = int(input("Digite um valor: "))
    if x == 0 or valor > valores[-1]:
        valores.append(valor)
        print("Adicionando o valor ao final da lista!")
    else:
        pos = 0
        while pos < len(valores):
            if valor <= valores[pos]:
                valores.insert(pos, x)
                print(f"Valor adicionado na posição {pos}")
                break
            pos += 1
print(f"Os valores digitados foram {valores}")