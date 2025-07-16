from random import *
from time import sleep

def maior_numero(num):
    maior = num[0]
    for i in range(len(num)):
        if num[i] > maior:
            maior = num[i]

    return maior

def tela(valores):
    print("-="*3, "Analisando os valores gerados", "=-"*3)
    for n in valores:
        print(n, end=" ")
        sleep(0.5)
    print(f"Foram informados ao todo {len(valores)} valores!")
    print(f"O Maior valor informado foi: {maior_numero(valores)}")

c = 0
while c < 4:
    valores = []
    numeros_gerados = randint(1,10)
    for i in range(numeros_gerados):
        valores.append(randint(1,10))
    tela(valores)
    c+=1