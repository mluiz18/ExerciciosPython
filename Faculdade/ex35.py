voto = int(input("Digite seu voto: "))
c1 = 0
c2 = 0
c3 = 0
c4 = 0
votos_brancos = 0
votos_nulos = 0

while voto != 0:
    if voto == 6:
        votos_brancos += 1
    else:
        if voto == 5:
            votos_nulos += 1
        else:
            if voto == 4:
                c4 += 1
            else:
                if voto == 3:
                    c3 += 1
                else:
                    if voto == 2:
                        c2 += 1
                    else:
                        if voto == 1:
                            c1 += 1
                        else:
                            print("Voto inválido!")
    voto = int(input("Digite seu voto: "))

print(f"Votos no candidato 1: {c1}")
print(f"Votos no candidato 2: {c2}")
print(f"Votos no candidato 3: {c3}")
print(f"Votos no candidato 4: {c4}")
print(f"Votos em branco: {votos_brancos}")
print(f"Votos nulos: {votos_nulos}")
