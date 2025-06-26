total_gasto = 0
produtos_mais_de_mil = 0
produto_mais_barato = ""
preco_mais_barato = 0
continuar = "S"
while True:
    nome = str(input("Digite o nome do produto: "))
    preco = float(input("Digite o preço do produto: "))
    if total_gasto == 0:
        produto_mais_barato = nome
        preco_mais_barato = preco
    else:
        if preco < preco_mais_barato:
            produto_mais_barato = nome
            preco_mais_barato = preco

    total_gasto += preco
    if preco >= 1000:
        produtos_mais_de_mil += 1

    continuar = str(input("Quer continuar? [S/N]: ")).upper()
    if continuar == "N":
        break

print(f"Total gasto na compra = R${total_gasto}")
print(f"Produtos que custam mais de R$1000 = {produtos_mais_de_mil}")
print(f"Nome do produto mais barato = {produto_mais_barato}")