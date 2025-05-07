from random import *
numero_maquina = randint(0,10)
numero_pessoa = int(input("Adivinhe o número: "))
tentativas = 1

if numero_pessoa == numero_maquina:
    print("Parebéns você acertou de primeira!")
else:
    while numero_maquina != numero_pessoa:
        tentativas += 1
        numero_pessoa = int(input("Adivinhe o número: "))
    print(f"Parabéns! Você conseguiu acertar com {tentativas} tentativas. ")