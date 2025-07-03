pessoas = []
dados = []

for i in range(5):
    dados.append(str(input("Nome: ")))
    dados.append(str(input("Idade: ")))
    pessoas.append(dados[:])
    dados.clear()

for p in pessoas:
    print(f"Nome: {p[0]} \nIdade: {p[1]} \n")