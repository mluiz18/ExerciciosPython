def ficha(nome="desconhecido", gols=0):
    """
    Função que retorna um print com o nome e quantidade de gols do jogador
    :param nome: nome
    :param gols: gols
    :return: print
    """
    if nome == "":
        nome="desconhecido"
    if gols == str():
        gols = 0
    print(f"O Jogador {nome} fez {gols} gol(s) no campeonato")

n = str(input("Nome: "))
g = int(input("Gols: "))
ficha(n,g)
