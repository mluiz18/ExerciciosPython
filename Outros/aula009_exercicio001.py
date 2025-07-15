def area(altura, largura):
    calculo = altura*largura
    print(f"A Área do retângulo ({altura}x{largura}) é de {calculo} m²")

alt = float(input("Digite a altura (m): "))
lar = float(input("Digite a largura (m): "))
area(alt,lar)