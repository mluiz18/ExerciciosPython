from random import *
vitoria = 0
while True:
    valor = int(input("Digite um valor: "))
    parouimpar = str(input("Par ou Impar [P/I]: ")).upper()
    valor_maquina = randint(1,10)
    soma = valor + valor_maquina

    resposta = ""
    if soma % 2 == 0:
        resposta = "Par"
        resultadodivisao = "P"
    else:
        resposta = "Impar"
        resultadodivisao = "I"

    print(f"Você jogou {valor}, a maquina jogou {valor_maquina}! No total deu {soma}, que é {resposta}!")

    if parouimpar == resultadodivisao:
        print("Você venceu!")
        vitoria += 1
    else:
        print("Você perdeu!")
        print(f"Você tinha uma sequência de  {vitoria} vitorias")
        break