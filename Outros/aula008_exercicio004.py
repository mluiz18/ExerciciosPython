dados = dict()
gols = []
dados["Nome"] = str(input("Nome do Jogador: "))
partidas = int(input("Partidas jogadas: "))
for x in range(partidas):
    gols.append(int(input(f"Quantos gols na partida {x+1}? ")))
dados["gols"] = gols[:]
s = 0
for i in range(len(gols)):
    s += gols[i]
dados["total"] = s
print("-="*3, f"DADOS DO JOGADOR {dados['Nome']}", "=-"*3)
print(dados)
print("-="*30)
for k,v in dados.items():
    print(f"campo {k} tem valor {v}")
print("-="*30)
print(f"O Jogador {dados['Nome']} jogou {partidas} partidas.")
for x in range(partidas):
    print(f"Partida {x+1}: {dados["gols"][x]} gols")
print(f"Foram no total {dados['total']} gols.")