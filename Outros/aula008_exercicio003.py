from datetime import datetime
cadastro = {}
cadastro["nome"] = str(input("Nome: "))
nascimento = int(input("Ano de Nascimento: "))
cadastro["idade"] = datetime.now().year - nascimento
cadastro["cpts"] = int(input("Carteira de Trabalho (0 não tem): "))
if cadastro["cpts"] != 0:
    cadastro["Ano de contratação"] = int(input("Ano de contratação: "))
    cadastro["Salário"] = float(input("Salário: "))
    cadastro["Aposentadoria"] = cadastro["idade"] + ((cadastro["Ano de contratação"] + 35) - datetime.now().year)

print("-="*3, "DADOS CADASTRADOS", "=-"*3)
for k,v in cadastro.items():
    print(f"{k} = {v}")