import aula011_utilidades as aula011

def resumo(p, a, r):
    aumento = aula011.aumentar(p, a)
    reducao = aula011.diminuir(p, r)
    metade = aula011.metade(p)
    dobro = aula011.dobro(p)

    print(f"-="*4, "RESUMO", "=-"*4)
    print(f"PREÇO: {aula011.moeda(p)}")
    print(f"METADE: {aula011.moeda(metade)}")
    print(f"DOBRO: {aula011.moeda(dobro)}")
    print(f"AUMENTO DE {a}%: {aula011.moeda(aumento)}")
    print(f"REDUÇÃO DE {r}%: {aula011.moeda(reducao)}")