dados = {}
banco = []
mulheres = []
c = 0
s_idade = 0
r = "S"
while r in "Ss":
    dados["nome"] = str(input("Nome: "))
    dados["idade"] = int(input("Idade: "))
    s_idade += dados["idade"]
    dados["Sexo"] = str(input("Sexo [M/F]: ")).title()
    while dados["Sexo"] not in "MmFf":
        print("ERRO! Opção inválida! Tente novamente.")
        dados["Sexo"] = str(input("Sexo [M/F]: ")).title()
    if dados["Sexo"] in "Ff":
        mulheres.append(dados.copy())
    banco.append(dados.copy())
    c += 1
    r = str(input("Quer continuar? [S/N] "))
    while r not in "SsNn":
        print("ERRO! Opção inválida! Tente novamente.")
        r = str(input("Quer continuar? [S/N] "))

media = s_idade/c
print("-="*3, "RESULTADO", "=-"*3)

if c == 1:
    print(f"Ao todo foram cadastrada {c} pessoa")
else:
    if c > 1:
        print(f"Ao todo foram cadastradas {c} pessoas")

print(f"A Média da idade foi de {media:.2f}")

if len(mulheres) == 0:
    print("Nenhuma mulher foi cadastrada!")
else:
    print(f"Uma lista com todas as mulheres cadastradas:")
    for m in range(len(mulheres)):
        print(f"Nome: {mulheres[m]['nome']}, Idade: {mulheres[m]['idade']}")

pessoas_idade_acima_da_media = []
for v in range(len(banco)):
    if banco[v]["idade"] >= media:
        pessoas_idade_acima_da_media.append(banco[v])

print(f"Lista de pessoas com idade acima da média ({media:.2f} anos):")
for i in range(len(pessoas_idade_acima_da_media)):
    print(f"Nome: {pessoas_idade_acima_da_media[i]['nome']}, Idade: {pessoas_idade_acima_da_media[i]['idade']}, Sexo: {pessoas_idade_acima_da_media[i]['Sexo']}")