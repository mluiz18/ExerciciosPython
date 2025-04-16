inicio = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razão da PA: "))
decimo = inicio+(10-1)*razao
for x in range(inicio, decimo+razao, razao):
    print(x)