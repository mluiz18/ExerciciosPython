from lib import menu
from time import sleep
from arquivo import *

arq = "cursoemvideo.txt"

if not arqExiste(arq):
    print("Arquivo Não existe")
    sleep(0.3)
    criarArquivo(arq)
    sleep(1)
    print("\n"*500)

while True:
    e = menu()
    if e == 1:
        lerArquivo(arq)
    else:
        if e == 2:
            nome = str(input("Nome: "))
            idade = int(input("Idade: "))
            cadastroArq(arq, nome, idade)
        else:
            if e == 3:
                print("-=" * 3, "SAINDO DO PROGRAMA", "=-" * 3)
                sleep(0.2)
                break