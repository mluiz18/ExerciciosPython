preco_normal = float(input("Qual o preço do produto: "))
condicao_de_pagamento = str(input("Qual a condição de pagamento: ")).title().strip()

if condicao_de_pagamento == "Cartão De Crédito" or condicao_de_pagamento == "Cartao De Credito":
    parcelamento = int(input("Quantas vezes vai parcelar: "))
    if parcelamento == 1:
        descontode5 = preco_normal - (preco_normal * 0.05)
        print(f"Você pagará 1x no cartão, o preço de R${descontode5}")
    elif parcelamento == 2:
        print(f"Você pagará 2x no cartão, o preço de R${preco_normal}")
    elif parcelamento >= 3:
        vintedejuros = preco_normal + (preco_normal * 0.20)
        print(f"Você pagará em {parcelamento}x no cartão, o preço de R${vintedejuros}")

elif condicao_de_pagamento == "A vista" or condicao_de_pagamento == "Dinheiro":
    descontode10 = preco_normal - (preco_normal * 0.10)
    print(f"Você pagará à vista, o preço de R${descontode10}")