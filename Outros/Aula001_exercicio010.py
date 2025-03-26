import random

sua_escolha = str(input("Escolha sua jogada (Pedra, Papel ou Tesoura): ")).title().strip()
pc_escolha = ("Pedra", "Papel", "Tesoura")
pc_jogada = random.choice(pc_escolha)

print(f"A Máquina jogou {pc_jogada}")

if sua_escolha  == "Pedra" and pc_jogada == "Papel":
    print("A Máquina venceu o jogo")
elif sua_escolha == "Papel" and pc_jogada == "Tesoura":
    print("A Máquina venceu o jogo")
elif sua_escolha == "Tesoura" and pc_jogada == "Pedra":
    print("A Máquina venceu o jogo")
elif sua_escolha == "Papel" and pc_jogada == "Pedra":
    print("Parabéns! você venceu!")
elif sua_escolha == "Tesoura" and pc_jogada == "Papel":
    print("Parabéns! você venceu!")
elif sua_escolha == "Pedra" and pc_jogada == "Tesoura":
    print("Parabéns! você venceu!")
else:
    print("Empate")
