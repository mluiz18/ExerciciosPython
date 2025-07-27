nomes = ["João", "Pedro", "Miguel", "Carlos", "Gustavo"]
nome = str(input("Digite um nome: ")).title()
presente = False
for i in range(len(nomes)):
    if nome == nomes[i]:
        presente = True
        break

if presente:
    print(f"O Nome '{nome}' está presente na lista!")
else:
    print(f"O Nome '{nome}' não está presente na lista!")