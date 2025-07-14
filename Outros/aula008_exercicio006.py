dados = {}
banco = []
r = "S"
while r in "Ss":
    dados["nome"] = str(input("Nome: "))
    partidas = int(input(f"Quantos jogos {dados['nome']} jogou? "))
    gols = []
    for x in range(partidas):
        gols.append(int(input(f"Quantos gols {dados['nome']} fez na partida {x+1}? ")))
    dados["gols"] = gols[:]
    dados["total"] = sum(gols)
    banco.append(dados.copy())
    r = str(input("Quer continuar? [S/N]")).upper()[0]
    while r not in "SN":
        print("Erro! Tente novamente.")
        r = str(input("Quer continuar? [S/N]")).upper()[0]

print("-="*3, "TABELA GERAL", "=-"*3)
c = 0
for c in range(len(banco)):
    print(f"cod: {c} Nome: {banco[c]['nome']} Gols: {banco[c]['gols']} Total:{banco[c]['total']}")
g = c
aux = int(input("ID do jogador [999 interrompe]: "))
if aux == 999:
    g = 999
while aux > g or aux < 0:
    print("Esse jogador não existe! Tente novamente.")
    aux = int(input("ID do jogador [999 interrompe]: "))
while aux != 999:
    print("-="*3, f"DADOS DO JOGADOR {banco[aux]['nome'].upper()}", "=-"*3)
    for c in range(len(banco[aux]['gols'])):
        print(f"Jogo {c+1} = {banco[aux]['gols'][c]}")

    aux = int(input("ID do jogador [999 interrompe]: "))
    if aux == 999:
        break
    while aux > g or aux < 0:
        print("Esse jogador não existe! Tente novamente.")
        aux = int(input("ID do jogador [999 interrompe]: "))